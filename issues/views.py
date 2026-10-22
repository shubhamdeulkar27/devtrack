import json
from typing import override
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from issues.models import CriticalIssue, Issue, LowPriorityIssue, Reporter


# Create your views here.
REPORTERS_FILE = 'issues/files/reporters.json'
ISSUES_FILE = 'issues/files/issues.json'

#Reporters Views
class ReporterViews(APIView):
    
    def __get_all_reporters(self):
        with open(REPORTERS_FILE, 'r') as file:
            data = json.loads(file.read())
        if isinstance(data, dict):
            data = [data]
        return [Reporter(**item) for item in data]

    @override
    def get(self, request):
        reporters = self.__get_all_reporters()
        reporter_id = request.query_params.get('id')
        if reporter_id is None:
            return Response(
                [r.to_dict() for r in reporters], 
                status=status.HTTP_200_OK)
        try:
            reporter_id = int(reporter_id)
        except (TypeError, ValueError):
            return Response({'error':'Invalid Id'}, status=status.HTTP_400_BAD_REQUEST)
        for reporter in reporters:
            if reporter.id == reporter_id:
                return Response(reporter.to_dict(), status=status.HTTP_200_OK)
        return Response({'error': 'Reporter not found'}, status=404)

    @override
    def post(self, request):
        data = request.data
        reporters = self.__get_all_reporters()
        reporter = Reporter(
                id = len(reporters) + 1,
                name = data.get('name'),
                email= data.get('email'),
                team = data.get('team')
            )
        try:
            reporter.validate()
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        payload = reporter.to_dict()
        with open(REPORTERS_FILE,'w') as file:
            json.dump([r.to_dict() for r in reporters] + [payload],file, indent = 2)
        return Response(payload, status = status.HTTP_201_CREATED)

#Issues Views
class IssueView(APIView):

    def __get_all_issues(self):
        with open(ISSUES_FILE, 'r') as file:
            data = json.loads(file.read())
        if isinstance(data, dict):
            data = [data]
        return [Issue(**item) for item in data]
    
    @override
    def get(self, request):
        issues = self.__get_all_issues()
        issue_id = request.query_params.get('id')
        issue_status = request.query_params.get('status')

        if issue_id:
            try:
                issue_id = int(issue_id)
            except(TypeError, ValueError):
                return Response({'error':'Invalid Id'}, status=status.HTTP_400_BAD_REQUEST)
            for issue in issues:
                if issue.id == issue_id:
                    return Response(issue.to_dict(), status=status.HTTP_200_OK)
        elif issue_status:
            issues = [ i for i in issues if i.status == issue_status]
            return Response(
                [i.to_dict() for i in issues],
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                [i.to_dict() for i in issues],
                status=status.HTTP_200_OK
            )
        return Response({'error' : 'issue not found'}, status = status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        issues = self.__get_all_issues()

        if data['priority'] == 'critical':
            issue = CriticalIssue(
                id = len(issues) + 1,
                title = data.get('title'),
                description = data.get('description'),
                status = data.get('status'),
                priority = data.get('priority'),
                reporter_id = data.get('reporter_id') 
            )
        elif data['priority'] == 'low':
            issue = LowPriorityIssue(
                id = len(issues) + 1,
                title = data.get('title'),
                description = data.get('description'),
                status = data.get('status'),
                priority = data.get('priority'),
                reporter_id = data.get('reporter_id') 
            )
        else:
            issue = Issue(
                id = len(issues) + 1,
                title = data.get('title'),
                description = data.get('description'),
                status = data.get('status'),
                priority = data.get('priority'),
                reporter_id = data.get('reporter_id') 
            )
        
        try:
            issue.validate()
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        payload = issue.to_dict()
        with open(ISSUES_FILE, 'w') as file:
            json.dump([i.to_dict() for i in issues] + [payload], file, indent = 2)
        return Response(payload, status = status.HTTP_201_CREATED)
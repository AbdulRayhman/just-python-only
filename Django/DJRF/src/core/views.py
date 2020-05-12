from django.http import JsonResponse
from django.shortcuts import render


def test_view(request):
		return JsonResponse({
			name: 'ABCD',
			age: 12,
			skills: ['A', 1, TRUE, {role: [1, 2, 3]}]
		}, safe=False)

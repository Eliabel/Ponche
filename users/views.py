from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assistant, Professor, Attendance
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, "theme/login.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({'status': 200})
        else:
            return HttpResponseBadRequest()


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/tables.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class DashboardView(APIView):
    @login_required
    def get(self, request, *args, **kwargs):
        user = request.user
        if Assistant.objects.filter(user=user).exists():
            return render(request, "users/assistantt/dashboard.html", {})
        elif Professor.objects.filter(user=user).exists():
            professor = Professor.objects.get(user=user)
            return render(request, "users/professor/dashboard.html", {'qr_code': professor.qr_code})
        else:
            return HttpResponseBadRequest()

class RecordAttendanceView(APIView):
    @login_required
    def post(self, request, qr_code):
        if Professor.objects.filter(qr_code=qr_code).exists():
            professor = Professor.objects.get(qr_code=qr_code)
            assistant = Assistant.objects.get(user=request.user)
            Attendance.objects.create(professor=professor, assistant=assistant)
            return Response({'status': 200})
        else:
            return HttpResponseBadRequest()
        
@staff_member_required
@csrf_exempt
def attendance_table(request):
    attendances = Attendance.objects.all()
    if request.method == 'POST':
        # Exportar la tabla de asistencia como un archivo CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="asistencia.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Profesor', 'Asistente', 'Fecha y hora'])

        for attendance in attendances:
            writer.writerow([attendance.id, attendance.professor.name, attendance.assistant.user.username, attendance.timestamp])

        return response
    else:
        return render(request, 'admin/attendance_table.html', {'attendances': attendances})




from django.shortcuts import render
from django.views.generic import View, TemplateView, UpdateView, DetailView

from User.forms import StudentRegisterForm, ParentForm
from User.models import Student
from User.mixins import AdminRequiredMixin


class DashboardRibbonView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/ribbon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = students = Student.objects.filter(
                                                    school__admin=self.request.user
                                                ).select_related('account', 'school', 'edu_grade')
        st_gender = students.values_list('gender')
        context["all"] = len(students)
        context["woman"] = list(st_gender).count(('woman',))
        context["man"] = list(st_gender).count(('man',))
        context["inactive"] = list(students.values_list('account__is_active')).count((False,))
        return context
    

class StudentDetailView(AdminRequiredMixin, View):
    template_name = 'dashboard/student-detail.html'

    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.select_related('account', 'school', 'edu_grade', 
                                                 'parent').get(pk=pk)
        return render(request, self.template_name, {'student': student})


class StudentUpdateView(AdminRequiredMixin, UpdateView):
    model = Student
    form_class = StudentRegisterForm
    template_name = 'dashboard/student-update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_parent"] = ParentForm
        return context
    

    
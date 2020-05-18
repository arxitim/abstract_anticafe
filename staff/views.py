from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout

from core.models import Table, Account, TableBookingQueue
from staff.decorators import staff_required


class ConfirmBooking(View):
    template_name = 'staff/confirm_booking.html'

    def get(self, request, booking_id):
        context = {}

        if request.user.is_staff:
            booking = TableBookingQueue.objects.get(pk=booking_id)
            table = booking.table
            table.is_busy = True
            table.save()

            context['status'] = True
            context['booking'] = booking
            context['table'] = table

            return render(request, self.template_name, context)
        else:
            return redirect('login')


class AddTable(FormView):
    template_name = 'staff/add_table.html'

    @staff_required
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

from django.shortcuts import render
from .forms import TicketForm

def ticket_form_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TicketForm()
    return render(request, 'ticket_form.html', {'form': form})

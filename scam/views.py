from django.http import Http404
from django.shortcuts import render, redirect

#import enchant
import re
from migrations.models import PhoneForm

# D = enchant.Dict("en-US")


def algorithm(a, b, c):
    s1, s = 0, 0
    a1 = list(PhoneForm.objects.values_list('email', flat=True))
    if len(a) > 7:
        if re.match(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', a):
            s = s + 1
        else:
            s = s + 0

    for item in a1:
        if a == item:
            s1 = s1 + 1
        else:
            s1 = s1 + 0
        if s1 > 2:
            return False
        else:
            e = list(PhoneForm.objects.filter(email=item).values_list('subjects', flat=True))
            for itm in e:
                if b == itm:
                    return False
                else:
                    f = list(PhoneForm.objects.filter(email=item).values_list('messages', flat=True))
                    for itm1 in f:
                        if c == itm1:
                            return False
                        else:
                            s = s + 1

    list1 = b.split(' ')
    l1 = len(list1)
    ln1 = 0
    for r in list1:
        if D.check(r) == True:
            ln1 = ln1 + 1
        else:
            ln1 = ln1 + 0
    if l1 == ln1:
        s = s + 1
    else:
        s = s + 0

    list2 = c.split(' ')
    l2 = len(list2)
    ln2 = 0
    for n in list2:
        if D.check(n) == True:
            ln2 = ln2 + 1
        else:
            ln2 = ln2 + 0
    if l2 == ln2:
        s = s + 1
    else:
        s = s + 0

    if s == 4:
         return True
    else:
        return False


def c_form(request):
    if request.method == 'GET':
        template = 'phone.html'
        x = PhoneForm.objects.all()
        data = {'phone_list': x}
        return render(request, template, data)

    elif request.method == 'POST':
        email = request.POST['email']
        subjects = request.POST['subjects']
        messages = request.POST['messages']
        if algorithm(email, subjects, messages):
            x = PhoneForm(email=email, subjects=subjects, messages=messages)
            x.save()
            return redirect('c_form')
        else:
            return redirect('c_form')


def c_form_delete(request, phone_id):
    try:
        x = PhoneForm.objects.get(id=phone_id)
    except PhoneForm.DoesNotExsist:
        return Http404
    else:
        x.delete()
        return redirect('c_form')

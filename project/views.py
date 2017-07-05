import random, hashlib

from oslo_i18n import translate as _
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import render_to_string

from domain.models import Domain
from project.models import Project
from project.forms import ProjectForm
from role.models import Assignment, Role
from sites.models import Sites
from user_profile.models import Profile

# email sending function
def send_email(con, subject, email_to, email_from):
    c = Context(con)
    text_content = render_to_string('mail/user_register_welcome.txt', c)
    html_content = render_to_string('mail/user_register_welcome.html', c)

    email = EmailMultiAlternatives(subject, text_content, email_from)
    email.attach_alternative(html_content, "text/html")
    email.to = [email_to]
    email.send()

@login_required
def project_select(request, project_id, user_id):
    user = Profile.objects.get(user_id=user_id)
    user.selected_project = project_id
    user.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            u = request.user
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]

            usernamesalt = request.user.email

            profile = Profile.objects.get(user_id=u.id)
            profile.activation_key = hashlib.sha1(salt + usernamesalt).hexdigest()
            profile.key_expires = timezone.now() + timedelta(days=2)

            domain = Domain.objects.create(
                name=form.cleaned_data['project'],
            )
            # create project for new user
            project = Project.objects.create(
                name=form.cleaned_data['project'],
                description='Project for %s ' % (u.username),
                domain=domain
            )

            # get role
            r = Role.objects.get(name="user")

            # assign new user as domain user
            assign_domain = Assignment.objects.create(
                type=3,
                actor=u,
                target_domain=domain,
                target_project=project,
                role=r
            )

            # assign new user as project user
            assign_project = Assignment.objects.create(
                type=1,
                actor=u,
                target_domain=domain,
                target_project=project,
                role=r,
            )

            # get first site
            site = Sites.objects.first()
            # get domain assignment
            domain = Assignment.objects.filter(actor=u.id)
            project = Assignment.objects.filter(actor=u.id)

            # get domain assignment
            domain = Assignment.objects.filter(actor=u.id)
            project = Assignment.objects.filter(actor=u.id)
            # if there is a site
            if site:
                # save site id to profile
                profile.selected_site = site.id
            profile.selected_domain = domain[0].target_domain_id
            profile.selected_project = project[0].target_project_id
            profile.save()

            # create domain for new user
            site_url = settings.SITE_ROOT_URL
            send_email({'u': u, 'profile': profile, 'site_url': site_url},
                       _('Welcome to our cloud'),
                       u.email,
                       settings.DEFAULT_EMAIL_FROM,
                       )
            return render(request,
                          'authcp/success.html',
                          {'u': u, 'profile': profile})

        else:
            print(form.errors)
    else:
        form = ProjectForm()

    title = _("Create Project")
    return render(request, 'project/create.html', {'form': form, 'title': title})

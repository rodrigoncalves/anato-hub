# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

from exam import Exam
from modeling.report import ReportStatus
from modeling.immunohistochemical import Immunohistochemical, \
    ImmunohistochemicalStatus, AntibodiesTable, ImmunohistochemicalReport
from modeling.citology import Citology, CitologyReport, CitologyStatus, \
    CitologyType
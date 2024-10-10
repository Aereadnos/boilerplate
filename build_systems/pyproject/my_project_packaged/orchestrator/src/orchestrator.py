#/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import glob
import tarfile
from utils.promptflow_client import PFGeneratorClient
import os
import sys 


from utils.cms_client import StrapiClient


class Course(PFGeneratorClient):
    def __init__(self, course_title, course_content):
        sc = StrapiClient()
        PFGeneratorClient.__init__(self)
        summary_content = self.generate_summary(language="english", text=course_topic)
        sc.post_lesson(lesson_text=summary_content)

#!/usr/bin/env python
# coding=utf-8
import web

urls = (
    "/data", "Data"
)

app_public = web.application(urls,locals())

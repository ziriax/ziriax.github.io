@echo off
docker run -p 4000:4000 -p 35729:35729 -v %cd%:/app blog


import subprocess
from pathlib import Path
from django.conf import settings

def git_revision(request):
    """
    Повертає короткий SHA поточного коміту або '' у разі помилки.
    """
    repo_dir = Path(settings.BASE_DIR)
    try:
        rev = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD'],
            cwd=repo_dir
        ).decode().strip()
    except Exception:
        rev = ''
    return {'git_revision': rev}
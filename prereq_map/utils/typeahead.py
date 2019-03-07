from prereq_map.models.currics import CurricTitles


def get_curric_typeahead():
    currics = CurricTitles.objects.all()
    curric_data = []
    for curric in currics:
        curric_data.append(curric.get_display_data())
    return curric_data


from django.db import models
from inflector import Inflector, English
from prereq_map.utils.process_data import CURRIC_BLACKLIST


class CurricTitles(models.Model):
    SEATTLE = 0
    BOTHELL = 1
    TACOMA = 2
    CAMPUS_CHOICES = (
        (SEATTLE, "Seattle"),
        (BOTHELL, "Bothell"),
        (TACOMA, "Tacoma")
    )
    abbrev = models.CharField(max_length=6)
    name = models.CharField(max_length=40)
    campus = models.SmallIntegerField(choices=CAMPUS_CHOICES)

    @staticmethod
    def update_titles(titles_dataframe):
        CurricTitles.objects.all().delete()
        title_objects = []
        for idx, row in titles_dataframe.iterrows():
            if row['curric_abbr'].strip() in CURRIC_BLACKLIST:
                continue
            inflect = Inflector(English)
            human_name = inflect.titleize(row['curric_full_nm'].strip())
            title_objects.append(
                CurricTitles(abbrev=row['curric_abbr'].strip(),
                             name=human_name,
                             campus=row['curric_branch'])
            )
        CurricTitles.objects.bulk_create(title_objects)

    def get_display_data(self):
        display_string = F"{self.get_campus_display()}: " \
                         F"{self.name} ({self.abbrev})"
        return {display_string: self.abbrev}

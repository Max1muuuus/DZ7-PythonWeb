from django.db import migrations


INITIAL_PLACES = [
    {
        "name": "Ivano-Frankivsk City Hall",
        "category": "Landmark",
        "description": "A historic city hall in the heart of the city, now home to the Museum of History.",
        "lat": 48.9226,
        "lng": 24.7111,
    },
    {
        "name": "Shevchenko Park",
        "category": "Park",
        "description": "A popular green space with walking paths, a lake, and recreational areas.",
        "lat": 48.9155,
        "lng": 24.7047,
    },
    {
        "name": "Potocki Palace",
        "category": "Historic site",
        "description": "The remains of a 17th-century palace complex associated with the city's founders.",
        "lat": 48.9228,
        "lng": 24.7068,
    },
    {
        "name": "Cathedral of the Holy Resurrection",
        "category": "Religious site",
        "description": "A landmark Greek Catholic cathedral located near the central square.",
        "lat": 48.9227,
        "lng": 24.7092,
    },
    {
        "name": "Bastion",
        "category": "Historic site",
        "description": "A restored section of the city's old defensive fortifications with shops and galleries.",
        "lat": 48.9205,
        "lng": 24.7103,
    },
]


def seed_initial_places(apps, schema_editor):
    Place = apps.get_model("places", "Place")
    Place.objects.using(schema_editor.connection.alias).bulk_create(
        [Place(**place) for place in INITIAL_PLACES]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_initial_places, migrations.RunPython.noop),
    ]

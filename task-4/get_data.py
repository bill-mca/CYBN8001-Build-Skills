import galah

print(galah.atlas_counts(filters=["year>=1980", "taxa=Banksia", "stateProvince=Australian Capital Territory"], group_by='year', expand=False))

print(galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False))

birds = galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False)

print(birds.sort_values('count', ascending=False).head(20))
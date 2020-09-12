import csv

with open("veg_table.csv", "r") as veg_table:
	veg_table_reader = csv.DictReader(veg_table)
	veg_name_to_id = {}
	for row in veg_table_reader:
		veg_name_to_id[row["name"]] = row["veg_id"]

with open("seed_outdoor.csv", "r") as seed_outdoor_table:
	seed_outdoor_table_reader = csv.DictReader(seed_outdoor_table)
	with open("seed_outdoor_edited.csv", "w") as seed_outdoor_edited:
		fieldnames = ["veg_id", "version", "month_id", "start_date", "through_date", "best"]
		seed_outdoor_table_writer = csv.DictWriter(seed_outdoor_edited, fieldnames = fieldnames)
		seed_outdoor_table_writer.writeheader()
		for row in seed_outdoor_table_reader:
			ID = veg_name_to_id[row['Veg_clean']]
			version = row['Version']
			month_id = row['MonthID']
			start_date = row['Start_day']
			through_date = row['Through']
			best = row['Best']

			if version == "":
				version = "seeds"
			if best == "":
				best = "No"


			if through_date == "":
				if month_id in ["4", "6", "9", "11"]:
					through_date = "30"
				elif month_id == "2":
					through_date = "28"
				else:
					through_date = "31"

			seed_outdoor_table_writer.writerow({"veg_id":ID, "version":version, "month_id":month_id, "start_date":start_date, "through_date":through_date, "best":best})


with open("seed_indoor.csv", "r") as seed_indoor_table:
	seed_indoor_table_reader = csv.DictReader(seed_indoor_table)
	with open("seed_indoor_edited.csv", "w") as seed_indoor_edited:
		fieldnames = ["veg_id", "version", "month_id", "start_date", "through_date", "best"]
		seed_indoor_table_writer = csv.DictWriter(seed_indoor_edited, fieldnames = fieldnames)
		seed_indoor_table_writer.writeheader()
		for row in seed_indoor_table_reader:
			ID = veg_name_to_id[row['Veg_clean']]
			version = row['Version']
			month_id = row['MonthID']
			start_date = row['Start_day']
			through_date = row['Through']
			best = row['Best']

			if version == "":
				version = "seeds"
			if best == "":
				best = "No"


			if through_date == "":
				if month_id in ["4", "6", "9", "11"]:
					through_date = "30"
				elif month_id == "2":
					through_date = "28"
				else:
					through_date = "31"

			seed_indoor_table_writer.writerow({"veg_id":ID, "version":version, "month_id":month_id, "start_date":start_date, "through_date":through_date, "best":best})


with open("starts.csv", "r") as starts_table:
	starts_table_reader = csv.DictReader(starts_table)
	with open("starts_edited.csv", "w") as starts_edited:
		fieldnames = ["veg_id", "month_id", "start_date", "through_date", "best"]
		starts_table_writer = csv.DictWriter(starts_edited, fieldnames = fieldnames)
		starts_table_writer.writeheader()
		for row in starts_table_reader:
			ID = veg_name_to_id[row['Veg_clean']]
			month_id = row['MonthID']
			start_date = row['Start_day']
			through_date = row['Through']
			best = row['Best']

			if best == "":
				best = "No"


			if through_date == "":
				if month_id in ["4", "6", "9", "11"]:
					through_date = "30"
				elif month_id == "2":
					through_date = "28"
				else:
					through_date = "31"

			starts_table_writer.writerow({"veg_id":ID, "month_id":month_id, "start_date":start_date, "through_date":through_date, "best":best})

with open("harvest.csv", "r") as harvest_table:
	harvest_table_reader = csv.DictReader(harvest_table)
	with open("harvest_edited.csv", "w") as harvest_edited:
		fieldnames = ["veg_id", "season_id"]
		harvest_table_writer = csv.DictWriter(harvest_edited, fieldnames = fieldnames)
		harvest_table_writer.writeheader()
		for row in harvest_table_reader:
			ID = veg_name_to_id[row['veg_name']]
			season = row['season_name']
			if season == "Fall":
				season_id = "4"
			elif season == "Winter":
				season_id = "1"
			elif season == "Summer":
				season_id = "3"
			else:
				season_id = "2"
			harvest_table_writer.writerow({"veg_id":ID, "season_id":season_id})

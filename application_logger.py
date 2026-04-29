import csv
import os


def log_application(hr_email, status):

    csv_file = "applications.csv"
    file_exists = os.path.isfile(csv_file)

    # mode='a' means "append" to the end of the file instead of overwriting
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write headers if this is the very first time running it
        if not file_exists:
            writer.writerow(["HR Email", "Application Status"])

        # Write the data
        writer.writerow([hr_email, status])
        print(f"📝 Logged to CSV: {hr_email} -> {status}")

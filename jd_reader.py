import os


def get_job_description(filename="jd.txt"):

    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                job_desc = file.read().strip()

            # Make sure the file isn't just empty
            if not job_desc:
                print(f"Warning: '{filename}' is empty. Please paste the JD into it.")
                return None

            return job_desc

        except Exception as e:
            print(f"Error reading the file: {e}")
            return None
    else:
        print(
            f"Error: Could not find '{filename}'. Please create it and paste your JD inside."
        )
        return None

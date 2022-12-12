# create or load dict if it exists
file_name = os.path.basename(input_path)
file_name = file_name.split('.')[0]
print(file_name)
output_path = output_path + "/" + file_name
if not os.path.exists(output_path):
    os.makedirs(output_path)
    os.makedirs(output_path + "/mask")
    os.makedirs(output_path + "/process")
names_of_video_samples_in_result_video_dict
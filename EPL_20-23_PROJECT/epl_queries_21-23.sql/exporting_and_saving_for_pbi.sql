-- Saving final dataset as csv for easy loading 
copy matches TO 'C:\temp\final_dataset_matches.csv' DELIMITER ',' CSV HEADER;

-- But will be connecting the datase directly to powerbi cause i will need to make use of few sql queries
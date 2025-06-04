 * Check target label encoding for disposition model ?
 * Anamoly: should be 'instance' level
 
Fields: cloudprovider, acc id, service name, instance id


## Requirements
## ------------------------------------------------------------------

* Python or Anaconda Software
* PgAdmin4 (PostgresSQL Database)
* Postman
* Git


## Setup 
## ------------------------------------------------------------------

* Software Installation:
    > Install Python or Anaconda software
    > Install PgAdmin4
    > Install Postman

* Git clone the "CloudCOEPredictionApp" application from "https://cloudcoepredictionapp-f3bvdbgqe5hqg4de.scm.eastus-01.azurewebsites.net:443/CloudCOEPredictionApp.git"
* Got to "CloudCOEPredictionApp/app/" directory and open the "config.py" file.
* Modify the database connection/credentials and save the file.


## Run
## ------------------------------------------------------------------

* Open "Anaconda Prompt" and go to the application directory.
* Run "pip install -r requirements.txt"
* Run "uvicorn main:app"
* For debugging, "uvicorn main:app --reload"


## API - Endpoints
## ------------------------------------------------------------------

* http://127.0.0.1:8000
* http://127.0.0.1:8000/v1/predict/disposition
* http://127.0.0.1:8000/v1/predict/anomalies
* http://127.0.0.1:8000/v1/predict/anomalies/<service_name>
* http://127.0.0.1:8000v1/predict/recommendation

Train the model:
* http://127.0.0.1:8000/v1/train/disposition
* http://127.0.0.1:8000/v1/train/anomalies
* http://127.0.0.1:8000/v1/train/anomalies/<service_name>
* http://127.0.0.1:8000v1/train/recommendation




INSERT INTO public.cloudrecommendationmaster (cloudprovider, servicename, pricingmodel, environment) VALUES
('Azure', 'Microsoft.Sql/servers',	'OnDemand',	'Prod'), ('AWS',	'Amazon Elastic File System',	'Reserved',	'Dev');

SELECT * FROM public.cloudrecommendationmaster
ORDER BY feature_id ASC 

-------------


INSERT INTO public.cloudfeaturerecommendations (feature_id, cpuusage, memoryusage,	diskusage, recommendation) VALUES
(1,	89,	78,	10, ''), (1, 27, 18, 11, ''), (2,	94,	23,	34, '');	

SELECT * FROM public.cloudfeaturerecommendations
ORDER BY recommendationid ASC 

import boto3

rds = boto3.client('rds')

response = rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t3.micro',
    DBInstanceIdentifier='mymysqlinstance',
    Engine='mysql',
    EngineVersion='8.0.35',
    LicenseModel='general-public-license',
    MasterUserPassword='botomj123456',
    MasterUsername='boto_user',
)

print(response)

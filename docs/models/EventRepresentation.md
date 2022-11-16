# phasetwo.model.event_representation.EventRepresentation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**time** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**realmId** | str,  | str,  |  | [optional] 
**organizationId** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**representation** | str,  | str,  |  | [optional] 
**operationType** | str,  | str,  |  | [optional] 
**resourcePath** | str,  | str,  |  | [optional] 
**resourceType** | str,  | str,  |  | [optional] 
**error** | str,  | str,  |  | [optional] 
**authDetails** | [**AuthDetailsRepresentation**](AuthDetailsRepresentation.md) | [**AuthDetailsRepresentation**](AuthDetailsRepresentation.md) |  | [optional] 
**[details](#details)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


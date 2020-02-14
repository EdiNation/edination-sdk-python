# Getting started

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=EdiNation%20API-Python)


## How to Use

The following section explains how to use the Edinationapi SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=EdiNation%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=EdiNation%20API-Python&projectName=edinationapi)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=EdiNation%20API-Python&projectName=edinationapi)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=EdiNation%20API-Python&projectName=edinationapi)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from edinationapi.edinationapi_client import EdinationapiClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=EdiNation%20API-Python&libraryName=edinationapi.edinationapi_client&projectName=edinationapi&className=EdinationapiClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=EdiNation%20API-Python&libraryName=edinationapi.edinationapi_client&projectName=edinationapi&className=EdinationapiClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| ocp_apim_subscription_key | API key to authenticate requests |



API client can be initialized as following.

```python
# Configuration parameters and credentials
ocp_apim_subscription_key = 'ocp_apim_subscription_key' # API key to authenticate requests

client = EdinationapiClient(ocp_apim_subscription_key)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [EdifactController](#edifact_controller)
* [EdiModelController](#edi_model_controller)
* [X12Controller](#x12_controller)

## <a name="edifact_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EdifactController") EdifactController

### Get controller instance

An instance of the ``` EdifactController ``` class can be accessed from the API Client.

```python
 edifact_controller = client.edifact
```

### <a name="read"></a>![Method: ](https://apidocs.io/img/method.png ".EdifactController.read") read

> Reads an EDIFACT file and returns its contents translated to an array of EdifactInterchange objects.

```python
def read(self,
                file_name,
                ignore_null_values=False,
                continue_on_error=False,
                char_set='utf-8',
                model=None,
                eancom_s_3=False)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fileName |  ``` Required ```  | Upload File |
| ignoreNullValues |  ``` Optional ```  ``` DefaultValue ```  | Whether to ignore all null values in the response. The default is false. |
| continueOnError |  ``` Optional ```  ``` DefaultValue ```  | Whether to continue reading if a corrupt interchange is encountered. The default is false. |
| charSet |  ``` Optional ```  ``` DefaultValue ```  | The encoding of the file contents. The default is utf-8. The available values are: unicodeFFFE, utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16. |
| model |  ``` Optional ```  | The model to use. By default, the API will infer the model based on the transaction and version identifiers. |
| eancomS3 |  ``` Optional ```  ``` DefaultValue ```  | The default syntax for EANCOM transactions. By default all EANCOM transactions will be translated and validated according to the rules of Syntax 4. Set this flag to true if you need Syntax 3 to be used. |



#### Example Usage

```python
file_name = open("pathtofile", 'rb')
ignore_null_values = False
continue_on_error = False
char_set = 'utf-8'
model = 'model'
eancom_s_3 = False

result = edifact_controller.read(file_name, ignore_null_values, continue_on_error, char_set, model, eancom_s_3)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="write"></a>![Method: ](https://apidocs.io/img/method.png ".EdifactController.write") write

> Translates an EdifactInterchange object to a raw EDIFACT interchange and returns it as a stream.

```python
def write(self,
                preserve_whitespace=False,
                char_set='utf-8',
                postfix=None,
                same_repetion_and_data_element=False,
                eancom_s_3=False,
                content_type='application/json',
                body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| preserveWhitespace |  ``` Optional ```  ``` DefaultValue ```  | Whether to preserve blank data elements so the output contains multiple delimiters instead of omitting any excess delimiters. The default is false. |
| charSet |  ``` Optional ```  ``` DefaultValue ```  | The encoding of the file contents. The default is utf-8. The available values are: unicodeFFFE, utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16. |
| postfix |  ``` Optional ```  | The postfix to be applied at the end of each segment, just after the segment separator. This is usually a carriage return (CR), line feed (LF) or both. By default, there is no postfix. |
| sameRepetionAndDataElement |  ``` Optional ```  ``` DefaultValue ```  | Sometimes the same delimiter is used to denote data element separator and repetition separator as in IATA transactions. By default, this is false. |
| eancomS3 |  ``` Optional ```  ``` DefaultValue ```  | The default syntax for EANCOM transactions. By default all EANCOM transactions will be translated and validated according to the rules of Syntax 4. Set this flag to true if you need Syntax 3 to be used. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The EdifactInterchange object to translate to raw EDIFACT. |



#### Example Usage

```python
preserve_whitespace = False
char_set = 'utf-8'
postfix = 'postfix'
same_repetion_and_data_element = False
eancom_s_3 = False
content_type = 'application/json'
body = EdifactInterchange()

result = edifact_controller.write(preserve_whitespace, char_set, postfix, same_repetion_and_data_element, eancom_s_3, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="validate"></a>![Method: ](https://apidocs.io/img/method.png ".EdifactController.validate") validate

> Validates an EdifactInterchange object according to the EDIFACT standard rules for each version and transaction.

```python
def validate(self,
                 syntax_set=None,
                 skip_trailer=False,
                 structure_only=False,
                 decimal_point='.',
                 eancom_s_3=False,
                 content_type='application/json',
                 body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| syntaxSet |  ``` Optional ```  | In case you need to validate against a syntax set, different than UNOA and UNOB, populate this filed with all of the allowed symbols, url-escaped.
            All data elements with alpha (A) or alphanumeric (AN) data types are validated against a syntax set of allowed characters. The supported syntax sets are UNOA and UNOB. The validator infers the correct syntax set from EdifactInterchange.UNB.SYNTAXIDENTIFIER_1.SyntaxIdentifier_1. The symbols added to this field will override the corresponding sets in both UNOA and UNOB. |
| skipTrailer |  ``` Optional ```  ``` DefaultValue ```  | You are allowed to validate an EdifactInterchange with missing interchange, functional group or transaction trailers (UNZ, UNE, UNT). This is because these will be automatically applied during the Write oprtaion so you don't have to worry about counting the items. By default it is expected that all trailers are present when you validate the EdifactInterchange and by default, this is set to false. To skip all trailer validation, set this to true. |
| structureOnly |  ``` Optional ```  ``` DefaultValue ```  | This is equivalent to HIPAA Snip level 1, where only the structure and control segments are validated. By default, this is set to false, however if you want to not validate things such as data types, number of repeteitions or dates, set this to true. |
| decimalPoint |  ``` Optional ```  ``` DefaultValue ```  | This could be either point . (default) or comma ,. |
| eancomS3 |  ``` Optional ```  ``` DefaultValue ```  | The default syntax for EANCOM transactions. By default all EANCOM transactions will be validated according to the rules of Syntax 4. Set this flag to true if you need Syntax 3 to be used. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The EdifactInterchange object to validate. |



#### Example Usage

```python
syntax_set = 'syntaxSet'
skip_trailer = False
structure_only = False
decimal_point = '.'
eancom_s_3 = False
content_type = 'application/json'
body = EdifactInterchange()

result = edifact_controller.validate(syntax_set, skip_trailer, structure_only, decimal_point, eancom_s_3, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="ack"></a>![Method: ](https://apidocs.io/img/method.png ".EdifactController.ack") ack

> Generates functional and/or technical CONTRL acknowledment(s) for the requested EdifactInterchange.

```python
def ack(self,
                syntax_set=None,
                detect_duplicates=False,
                tran_ref_number=1,
                interchange_ref_number=1,
                ack_for_valid_trans=False,
                batch_acks=True,
                technical_ack=None,
                eancom_s_3=False,
                content_type='application/json',
                body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| syntaxSet |  ``` Optional ```  | In case you need to validate against a syntax set, different than UNOA and UNOB, populate this filed with all of the allowed symbols, url-escaped. All data elements with alpha (A) or alphanumeric (AN) data types are validated against a syntax set of allowed characters. The supported syntax sets are UNOA and UNOB. The validator infers the correct syntax set from EdifactInterchange.UNB.SYNTAXIDENTIFIER_1.SyntaxIdentifier_1. The symbols added to this field will override the corresponding sets in both UNOA and UNOB. |
| detectDuplicates |  ``` Optional ```  ``` DefaultValue ```  | If you need to detect duplicates as in functional groups or transactions with the same reference number, set this flag to true. The default is false. |
| tranRefNumber |  ``` Optional ```  ``` DefaultValue ```  | The default is 1. Set this to whatever the CONTRL UNH.MessageReferenceNumber_01 needs to be. |
| interchangeRefNumber |  ``` Optional ```  ``` DefaultValue ```  | The default is 1. Set this to whatever the CONTRL EdifactInterchange.UNB.InterchangeControlReference_5 needs to be. |
| ackForValidTrans |  ``` Optional ```  ``` DefaultValue ```  | The default is false. Set this to true if you need UCM loops included for all valid transaction as well. By default UCM loops are generated only for invalid transactions. |
| batchAcks |  ``` Optional ```  ``` DefaultValue ```  | The default is true. Set this to false if you need to generate separate EdifactInterchange for each acknowledgment. By default all acknowledgments are batched in the same EdifactInterchange. |
| technicalAck |  ``` Optional ```  | The default technical acknowledgment CONTRL is generated according to EdifactInterchange.UNB.AcknowledgementRequest_9. You can either enforce it to always generate technical CONTRLs or supress it to never generate any technical CONTRLs. This will override the flag in EdifactInterchange.UNB.AcknowledgementRequest_9.
            The available values are: default, enforce, suppress. |
| eancomS3 |  ``` Optional ```  ``` DefaultValue ```  | The default syntax for EANCOM transactions. By default all EANCOM transactions will be validated according to the rules of Syntax 4. Set this flag to true if you need Syntax 3 to be used. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The EdifactInterchange object to acknowledge. |



#### Example Usage

```python
syntax_set = 'syntaxSet'
detect_duplicates = False
tran_ref_number = 1
interchange_ref_number = 1
ack_for_valid_trans = False
batch_acks = True
technical_ack = 'technicalAck'
eancom_s_3 = False
content_type = 'application/json'
body = EdifactInterchange()

result = edifact_controller.ack(syntax_set, detect_duplicates, tran_ref_number, interchange_ref_number, ack_for_valid_trans, batch_acks, technical_ack, eancom_s_3, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




[Back to List of Controllers](#list_of_controllers)

## <a name="edi_model_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EdiModelController") EdiModelController

### Get controller instance

An instance of the ``` EdiModelController ``` class can be accessed from the API Client.

```python
 edi_model_controller = client.edi_model
```

### <a name="upload"></a>![Method: ](https://apidocs.io/img/method.png ".EdiModelController.upload") upload

> Uploads a model file to a subscription. It must be a valid DOT NET assembly.

```python
def upload(self,
                file_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fileName |  ``` Required ```  | Upload File |



#### Example Usage

```python
file_name = open("pathtofile", 'rb')

edi_model_controller.upload(file_name)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="get_models"></a>![Method: ](https://apidocs.io/img/method.png ".EdiModelController.get_models") get_models

> Retrieves all models for a subscription.

```python
def get_models(self,
                   system=True)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| system |  ``` Optional ```  ``` DefaultValue ```  | Whether to retrieve EdiNation's or custom uploaded models. |



#### Example Usage

```python
system = True

result = edi_model_controller.get_models(system)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="get_model"></a>![Method: ](https://apidocs.io/img/method.png ".EdiModelController.get_model") get_model

> Retrieve a particular model file as a stream.

```python
def get_model(self,
                  id,
                  system=True)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The model name. |
| system |  ``` Optional ```  ``` DefaultValue ```  | Whether to search in EdiNation's or custom uploaded models. |



#### Example Usage

```python
id = 'id'
system = True

result = edi_model_controller.get_model(id, system)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="delete"></a>![Method: ](https://apidocs.io/img/method.png ".EdiModelController.delete") delete

> Deletes a particular model from the custom models.

```python
def delete(self,
                id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The model name. |



#### Example Usage

```python
id = 'id'

edi_model_controller.delete(id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




[Back to List of Controllers](#list_of_controllers)

## <a name="x12_controller"></a>![Class: ](https://apidocs.io/img/class.png ".X12Controller") X12Controller

### Get controller instance

An instance of the ``` X12Controller ``` class can be accessed from the API Client.

```python
 x_12_controller = client.x_12
```

### <a name="read"></a>![Method: ](https://apidocs.io/img/method.png ".X12Controller.read") read

> Reads an X12 file and returns its contents translated to an array of X12Interchange objects.

```python
def read(self,
                file_name,
                ignore_null_values=False,
                continue_on_error=False,
                char_set='utf-8',
                model=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| fileName |  ``` Required ```  | Upload File |
| ignoreNullValues |  ``` Optional ```  ``` DefaultValue ```  | Whether to ignore all null values in the response. The default is false. |
| continueOnError |  ``` Optional ```  ``` DefaultValue ```  | Whether to continue reading if a corrupt interchange is encountered. The default is false. |
| charSet |  ``` Optional ```  ``` DefaultValue ```  | The encoding of the file contents. The default is utf-8. The available values are: unicodeFFFE, utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16. |
| model |  ``` Optional ```  | The model to use. By default, the API will infer the model based on the transaction and version identifiers. |



#### Example Usage

```python
file_name = open("pathtofile", 'rb')
ignore_null_values = False
continue_on_error = False
char_set = 'utf-8'
model = 'model'

result = x_12_controller.read(file_name, ignore_null_values, continue_on_error, char_set, model)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="write"></a>![Method: ](https://apidocs.io/img/method.png ".X12Controller.write") write

> Translates an X12Interchange object to a raw X12 interchange and returns it as a stream.

```python
def write(self,
                preserve_whitespace=False,
                char_set='utf-8',
                postfix=None,
                content_type='application/json',
                body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| preserveWhitespace |  ``` Optional ```  ``` DefaultValue ```  | Whether to preserve blank data elements so the output contains multiple delimiters instead of omitting any excess delimiters. The default is false. |
| charSet |  ``` Optional ```  ``` DefaultValue ```  | The encoding of the file contents. The default is utf-8. The available values are: unicodeFFFE, utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16. |
| postfix |  ``` Optional ```  | The postfix to be applied at the end of each segment, just after the segment separator. This is usually a carriage return (CR), line feed (LF) or both. By default, there is no postfix. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The X12Interchange object to translate to raw X12. |



#### Example Usage

```python
preserve_whitespace = False
char_set = 'utf-8'
postfix = 'postfix'
content_type = 'application/json'
body = X12Interchange()

result = x_12_controller.write(preserve_whitespace, char_set, postfix, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="validate"></a>![Method: ](https://apidocs.io/img/method.png ".X12Controller.validate") validate

> Validates an X12Interchange object according to the X12 standard rules for each version and transaction.

```python
def validate(self,
                 basic_syntax=False,
                 syntax_set=None,
                 skip_trailer=False,
                 structure_only=False,
                 content_type='application/json',
                 body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| basicSyntax |  ``` Optional ```  ``` DefaultValue ```  | All data elements with alpha (A) or alphanumeric (AN) data types are validated against a syntax set of allowed characters. The default syntax set is the Extended, hence the default for this parameter is false. By setting this to true, validation will use the Basic syntax set. |
| syntaxSet |  ``` Optional ```  | In case you need to validate against a syntax set, different than Basic and Extended, populate this filed with all of the allowed symbols, url-escaped. |
| skipTrailer |  ``` Optional ```  ``` DefaultValue ```  | You are allowed to validate an X12Interchange with missing interchange, functional group or transaction trailers (IEA, GE, SE). This is because these will be automatically applied during the Write oprtaion so you don't have to worry about counting the items. By default it is expected that all trailers are present when you validate the X12Interchange and by default, this is set to false. To skip all trailer validation, set this to true. |
| structureOnly |  ``` Optional ```  ``` DefaultValue ```  | This is equivalent to HIPAA Snip level 1, where only the structure and control segments are validated. By default, this is set to false, however if you want to not validate things such as data types, number of repeteitions or dates, set this to true. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The X12Interchange object to validate. |



#### Example Usage

```python
basic_syntax = False
syntax_set = 'syntaxSet'
skip_trailer = False
structure_only = False
content_type = 'application/json'
body = X12Interchange()

result = x_12_controller.validate(basic_syntax, syntax_set, skip_trailer, structure_only, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




### <a name="ack"></a>![Method: ](https://apidocs.io/img/method.png ".X12Controller.ack") ack

> Generates functional/implementation and/or technical acknowledment(s) for the requested X12Interchange.

```python
def ack(self,
                basic_syntax=False,
                syntax_set=None,
                detect_duplicates=False,
                tran_ref_number=1,
                interchange_ref_number=1,
                ack_for_valid_trans=False,
                batch_acks=True,
                technical_ack=None,
                ack='997',
                ak_901_is_p=False,
                content_type='application/json',
                body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| basicSyntax |  ``` Optional ```  ``` DefaultValue ```  | All data elements with alpha (A) or alphanumeric (AN) data types are validated against a syntax set of allowed characters. The default syntax set is the Extended, hence the default for this parameter is false. By setting this to true, validation will use the Basic syntax set. |
| syntaxSet |  ``` Optional ```  | In case you need to validate against a syntax set, different than Basic and Extended, populate this filed with all of the allowed symbols, url-escaped. |
| detectDuplicates |  ``` Optional ```  ``` DefaultValue ```  | If you need to detect duplicates as in functional groups or transactions with the same reference number, set this flag to true. The default is false. |
| tranRefNumber |  ``` Optional ```  ``` DefaultValue ```  | The default is 1. Set this to whatever the 997 or 999 X12Interchange.ST.TransactionSetControlNumber_02 needs to be. In case there are multiple acknowledgments (for multiple functional groups), this will be starting reference number and every subsequent acknowledgment will have the previous reference number incremented with 1. |
| interchangeRefNumber |  ``` Optional ```  ``` DefaultValue ```  | The default is 1. Set this to whatever the 997 or 999 X12Interchange.ISA.InterchangeControlNumber_13 needs to be. |
| ackForValidTrans |  ``` Optional ```  ``` DefaultValue ```  | The default is false. Set this to true if you need AK2 loops included for all valid transaction as well. By default AK2 loops are generated only for invalid transactions. |
| batchAcks |  ``` Optional ```  ``` DefaultValue ```  | The default is true. Set this to false if you need to generate separate X12Interchange for each acknowledgment. By default all acknowledgments are batched in the same X12Interchange. |
| technicalAck |  ``` Optional ```  | The default technical acknowledgment TA1 is generated according to X12Interchange.ISA.AcknowledgementRequested_14. You can either enforce it to always generate TA1s or supress it to never generate any TA1s. This will override the flag in X12Interchange.ISA.AcknowledgementRequested_14.
            The available values are: default, enforce, suppress. |
| ack |  ``` Optional ```  ``` DefaultValue ```  | The default value is 997. The type of acknowledgment being generated. Set this to 999 if you need to generate an implementation instead of functional acknowledgment. The available values are: 997, 999. |
| ak901isP |  ``` Optional ```  ``` DefaultValue ```  | The value of the AK9's first element. By default it is "E". Set this to true if you want this value to be "P" instead. |
| contentType |  ``` Optional ```  ``` DefaultValue ```  | TODO: Add a parameter description |
| body |  ``` Optional ```  | The X12Interchange object to acknowledge. |



#### Example Usage

```python
basic_syntax = False
syntax_set = 'syntaxSet'
detect_duplicates = False
tran_ref_number = 1
interchange_ref_number = 1
ack_for_valid_trans = False
batch_acks = True
technical_ack = 'technicalAck'
ack = '997'
ak_901_is_p = False
content_type = 'application/json'
body = X12Interchange()

result = x_12_controller.ack(basic_syntax, syntax_set, detect_duplicates, tran_ref_number, interchange_ref_number, ack_for_valid_trans, batch_acks, technical_ack, ack, ak_901_is_p, content_type, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Bad Request |
| 500 | Server Error |




[Back to List of Controllers](#list_of_controllers)




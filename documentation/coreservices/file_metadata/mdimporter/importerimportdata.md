# ImporterImportData

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer toan importer import callback that imports importers.

## Declaration

```c
typedef Boolean (* ImporterImportData)
(
void *thisInterface,
CFMutableDictionaryRef attributes,
CFStringRef contentTypeUTI,
CFStringRef pathToFile
)
```

#### Return Value

Your callback functionshould return `true` if the metadatawas successfully returned, `false` ifthe metadata was not returned.

## Parameters

- `thisInterface`: The CFPlugin object that is called. This value is passed to the callback function.
- `attributes`: A mutable dictionary that you should populate with the metadata key/value pairs. This dictionary is created and passed to the callback function.
- `contentTypeUTI`: The content type of the file as a uniform type identifier. This value is passed to the callback function.
- `pathToFile`: The full path to the file. This value is passed to the callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdimporter/importerimportdata)*
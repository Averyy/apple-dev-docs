# Data Not Wanted Constants

**Framework**: Application Services  
**Kind**: enum

Constants your application can use to indicate it does not need certain types of data returned by various printing functions.

## Declaration

```c
#define kPMNoData  NULL
#define kPMDontWantSize  NULL
#define kPMDontWantData  NULL
#define kPMDontWantBoolean  NULL
#define kPMNoPrintSettings  NULL
#define kPMNoPageFormat  NULL
#define kPMNoReference  NULL
```

## Topics

### Constants
- [kPMNoData](./data_not_wanted_constants/kpmnodata.md)
  Specifies that your application does not need data returned for a particular parameter. For future compatibility, you are encouraged to use one of the following constants in cases where a specific type of data is not required.
- [kPMDontWantSize](./data_not_wanted_constants/kpmdontwantsize.md)
  Specifies that your application does not need the size information returned by the printing function.
- [kPMDontWantData](./data_not_wanted_constants/kpmdontwantdata.md)
  Specifies that your application does not need the data returned by the printing function.
- [kPMDontWantBoolean](./data_not_wanted_constants/kpmdontwantboolean.md)
  Specifies that your application does not need a Boolean value returned by the printing function.
- [kPMNoPrintSettings](./data_not_wanted_constants/kpmnoprintsettings.md)
  Specifies that your application does not need a `PMPrintSettings` object returned by the printing function.
- [kPMNoPageFormat](./data_not_wanted_constants/kpmnopageformat.md)
  Specifies that your application does not need a `PMPageFormat` object returned by the printing function.
- [kPMNoReference](./data_not_wanted_constants/kpmnoreference.md)
  Specifies that your application does not need a reference returned by the printing function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/data_not_wanted_constants)*
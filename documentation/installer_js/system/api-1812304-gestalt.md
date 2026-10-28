# gestalt

**Framework**: Installer JS  
**Kind**: uid

Provides gestalt information that corresponds to the given selector.

## Declaration

```
gestalt(selector)
```

## Return Value

Data for the given selector. 

## Overview

For example, the expression in [Listing 1](./api-1812304-gestalt.md#2556491) returns `'1040'` in OS X v10.4.0:

```javascript
system.gestalt('sysv').toString(16)
```

See [Gestalt Manager](../../coreservices/carbon_core/gestalt_manager.md) for detailed information.

> ⚠️ **Warning**: The underlying Gestalt Manager API is deprecated; use [version](./api-1812284-version.md) and [sysctl](./api-1812308-sysctl.md) instead of this function.

## Parameters

- `selector`: String specifying the selector for the data to retrieve.

## See Also

### Legacy Methods
- [localizedStandardString](./api-1812330-localizedstandardstring.md)
  Provides the localized standard string in the installation package for the current locale for a given key. 
- [localizedStandardStringWithFormat](./api-1812341-localizedstandardstringwithforma.md)
  Provides the formatted localized standard string in the installation package for the current locale, for a given key and a set of additional arguments. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/system/1812304-gestalt)*
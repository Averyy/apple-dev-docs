# System

**Framework**: Installer JS  
**Kind**: uid

An object that provides access to information about the target host. 

#### Overview

This object is accessed using the `system` global variable.

## Topics

### Accessing System Information
- [sysctl](system/1812308-sysctl.md)
  Provides the result of a `sysctlbyname()` call using the given selector.
- [users.desktopSessionCount](system/1812277-users_desktopsessioncount.md)
  The number of logged-in users.
- [version](system/1812284-version.md)
  A dictionary (associative array) with information about the current system version.
### Accessing Application Information
- [applications](system/1812235-applications.md)
  An object providing methods to obtain information about running applications.
### Accessing Files
- [files](system/1812262-files.md)
  An object providing file-access methods.
### Accessing IORegistry
- [ioregistry](system/1812270-ioregistry.md)
  An object providing access to the IOKit registry.
### Accessing Defaults
- [defaults](system/1812245-defaults.md)
  A dictionary representing the defaults system.
### Accessing Object Properties
- [propertiesOf](system/1812294-propertiesof.md)
  Provides an array containing the properties of a given object.
### Comparing Version Number Strings
- [compareVersions](system/1812314-compareversions.md)
  Provides the result of comparing two given version strings (for example, `'10.3.1'` and `'10.4'`).
### Internationalizing Distributions
- [localizedString](system/1812321-localizedstring.md)
  Provides the localized string in the installation package for the current locale for a given key.
- [localizedStringWithFormat](system/1812327-localizedstringwithformat.md)
  Provides the formatted localized string in the installation package for the current locale, for a given key and a set of additional arguments.
### Logging
- [log](system/1812348-log.md)
  Generates an Installer log entry with the `JS:` prefix.
### Running Programs
- [run](system/1812364-run.md)
  Launches a given program in the `Resources` directory of the installation package.
- [runOnce](system/1812367-runonce.md)
  Launches a given program in the `Resources` directory of the installation package, if it has not been run already.
### Legacy Methods
- [gestalt](system/1812304-gestalt.md)
  Provides gestalt information that corresponds to the given selector.
- [localizedStandardString](system/1812330-localizedstandardstring.md)
  Provides the localized standard string in the installation package for the current locale for a given key. 
- [localizedStandardStringWithFormat](system/1812341-localizedstandardstringwithforma.md)
  Provides the formatted localized standard string in the installation package for the current locale, for a given key and a set of additional arguments. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/system)*
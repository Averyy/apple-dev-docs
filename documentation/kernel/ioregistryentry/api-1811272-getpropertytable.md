# getPropertyTable

**Framework**: Kernel  
**Kind**: instm

Unsynchronized accessor to a registry entry's property table.

## Declaration

```c
OSDictionary * getPropertyTable(
 void ) const;
```

#### Return Value

A pointer to the property table as an OSDictionary. The pointer is valid while the registry entry is retained, and should not be released by the caller.

#### Overview

This method will return a pointer to the live property table as an OSDictionery. Its use is not recommended in most cases, instead use the synchronized accessors and helper functions of IORegistryEntry to access properties. It can only safely be used by one thread, which usually means it can only be used before a registry entry is entered into the registry.

## See Also

### Miscellaneous
- [attachToChild](./api-1810177-attachtochild.md)
  Method called in the parent entry when a child attaches.
- [attachToParent](./api-1810196-attachtoparent.md)
  Attaches a entry to a parent entry in a plane.
- [childFromPath](./api-1810215-childfrompath.md)
  Looks up a registry entry by relative path.
- [compareName](./api-1810236-comparename.md)
  Compares the name of the entry with one name, and optionally returns the matching name.
- [compareNames](./api-1810259-comparenames.md)
  Compares the name of the entry with one or more names, and optionally returns the matching name.
- [copyChildEntry](./api-1810279-copychildentry.md)
  Returns an registry entry's first child entry in a plane. Available in macOS 10.1 or later.
- [copyLocation](./api-1810296-copylocation.md)
  Returns the location string assigned to the registry entry as an OSSymbol.
- [copyName](./api-1810315-copyname.md)
  Returns the name assigned to the registry entry as an OSSymbol.
- [copyParentEntry](./api-1810335-copyparententry.md)
  Returns an registry entry's first parent entry in a plane. Available in macOS 10.1 or later.
- [copyProperty(const char *)](./api-1810352-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const char *, const IORegistryPlane *, IOOptionBits)](./api-1810371-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [copyProperty(const OSString *)](./api-1810386-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const OSString *, const IORegistryPlane *, IOOptionBits)](./api-1810403-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [copyProperty(const OSSymbol *)](./api-1810428-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const OSSymbol *, const IORegistryPlane *, IOOptionBits)](./api-1810451-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [dealiasPath](./api-1810478-dealiaspath.md)
  Strips any aliases from the head of path and returns the full path.
- [detachAbove](./api-1810509-detachabove.md)
  Detaches an entry from all its parent entries in a plane.
- [detachAll](./api-1810550-detachall.md)
  Detaches an entry and all its children recursively in a plane.
- [detachFromChild](./api-1810594-detachfromchild.md)
  Detaches a child entry from its parent in a plane.
- [detachFromParent](./api-1810632-detachfromparent.md)
  Detaches an entry from a parent entry in a plane.
- [dictionaryWithProperties](./api-1810672-dictionarywithproperties.md)
  Synchronized method to obtain copy a registry entry's property table.
- [free](./api-1810704-free.md)
  Standard free method for all IORegistryEntry subclasses.
- [fromPath(const char *, const IORegistryPlane *, char *, int *)](./api-1810742-frompath.md)
  Looks up a registry entry by relative path.
- [fromPath(const char *, const IORegistryPlane *, char *, int *, IORegistryEntry *)](./api-1810796-frompath.md)
  Looks up a registry entry by path.
- [getChildEntry](./api-1810842-getchildentry.md)
  Returns an registry entry's first child entry in a plane.
- [getChildIterator](./api-1810873-getchilditerator.md)
  Returns an iterator over an registry entry's child entries in a plane.
- [getDepth](./api-1810910-getdepth.md)
  Counts the maximum number of entries between an entry and the registry root, in a plane.
- [getGenerationCount](./api-1810941-getgenerationcount.md)
  Returns an generation count for all registry changing operations.
- [getLocation](./api-1810970-getlocation.md)
  Returns the location string assigned to the registry entry as a C-string.
- [getName](./api-1810990-getname.md)
  Returns the name assigned to the registry entry as a C-string.
- [getParentEntry](./api-1811012-getparententry.md)
  Returns an registry entry's first parent entry in a plane.
- [getParentIterator](./api-1811037-getparentiterator.md)
  Returns an iterator over an registry entry's parent entries in a specified plane.
- [getPath](./api-1811074-getpath.md)
  Create a path for a registry entry.
- [getPathComponent](./api-1811114-getpathcomponent.md)
  Create a path component for a registry entry.
- [getPlane](./api-1811147-getplane.md)
  Looks up the plane object by a C-string name.
- [getProperty(const char *)](./api-1811182-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const char *, const IORegistryPlane *, IOOptionBits)](./api-1811215-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getProperty(const OSString *)](./api-1811230-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const OSString *, const IORegistryPlane *, IOOptionBits)](./api-1811244-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getProperty(const OSSymbol *)](./api-1811254-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const OSSymbol *, const IORegistryPlane *, IOOptionBits)](./api-1811263-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getRegistryEntryID](./api-1811281-getregistryentryid.md)
  Returns an ID for the registry entry that is global to all tasks.
- [getRegistryRoot](./api-1811288-getregistryroot.md)
  Returns a pointer to the root instance of the registry.
- [init](./api-1811299-init.md)
  Standard init method for all IORegistryEntry subclasses.
- [inPlane](./api-1811307-inplane.md)
  Determines whether a registry entry is attached in a plane.
- [isChild](./api-1811317-ischild.md)
  Determines whether a registry entry is the child of another in a plane.
- [isParent](./api-1811327-isparent.md)
  Determines whether a registry entry is the parent of another in a plane.
- [makePlane](./api-1811335-makeplane.md)
  Constructs an IORegistryPlane object.
- [removeProperty](./api-1811343-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [removeProperty(const OSString *)](./api-1811354-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [removeProperty(const OSSymbol *)](./api-1811362-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [runPropertyAction](./api-1811370-runpropertyaction.md)
  Single thread a call to an action w.r.t. the property lock
- [serializeProperties](./api-1811384-serializeproperties.md)
  Synchronized method to serialize a registry entry's property table.
- [setLocation](./api-1811397-setlocation.md)
  Sets a location string for the registry entry, in a particular plane, or globally.
- [setName(const char *, const IORegistryPlane *)](./api-1811407-setname.md)
  Sets a name for the registry entry, in a particular plane, or globally.
- [setName(const OSSymbol *, const IORegistryPlane *)](./api-1811420-setname.md)
  Sets a name for the registry entry, in a particular plane, or globally.
- [setProperties](./api-1811430-setproperties.md)
  Optionally supported external method to set properties in a registry entry.
- [setProperty](./api-1811442-setproperty.md)
  Synchronized method to construct and add an OSData property to a registry entry's property table.
- [setProperty(const char *, bool)](./api-1811451-setproperty.md)
  Synchronized method to construct and add an OSBoolean property to a registry entry's property table.
- [setProperty(const char *, const char *)](./api-1811461-setproperty.md)
  Synchronized method to construct and add a OSString property to a registry entry's property table.
- [setProperty(const char *, OSObject *)](./api-1811476-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setProperty(const char *, unsigned long long, unsigned int)](./api-1811491-setproperty.md)
  Synchronized method to construct and add an OSNumber property to a registry entry's property table.
- [setProperty(const OSString *, OSObject *)](./api-1811507-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setProperty(const OSSymbol *, OSObject *)](./api-1811520-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setPropertyTable](./api-1811536-setpropertytable.md)
  Replace a registry entry's property table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryentry/1811272-getpropertytable)*
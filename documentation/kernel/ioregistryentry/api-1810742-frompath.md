# fromPath(const char *, const IORegistryPlane *, char *, int *)

**Framework**: Kernel  
**Kind**: instm

Looks up a registry entry by relative path.

## Declaration

```swift
virtual IORegistryEntry * childFromPath(
 const char *path, 
 const IORegistryPlane *plane = 0, 
 char *residualPath = 0, 
 int *residualLength = 0 );
```

#### Return_value

See IORegistryEntry::fromPath.

#### Overview

This function looks up a entry below the called entry by a relative path. It is just a convenience that calls IORegistryEntry::fromPath with this as the fromEntry parameter.

## Parameters

- `path`: See IORegistryEntry::fromPath.
- `plane`: See IORegistryEntry::fromPath.
- `residualPath`: See IORegistryEntry::fromPath.
- `residualLength`: See IORegistryEntry::fromPath.

## See Also

- [attachToChild](ioregistryentry/1810177-attachtochild.md)
  Method called in the parent entry when a child attaches.
- [attachToParent](ioregistryentry/1810196-attachtoparent.md)
  Attaches a entry to a parent entry in a plane.
- [childFromPath](ioregistryentry/1810215-childfrompath.md)
  Looks up a registry entry by relative path.
- [compareName](ioregistryentry/1810236-comparename.md)
  Compares the name of the entry with one name, and optionally returns the matching name.
- [compareNames](ioregistryentry/1810259-comparenames.md)
  Compares the name of the entry with one or more names, and optionally returns the matching name.
- [copyChildEntry](ioregistryentry/1810279-copychildentry.md)
  Returns an registry entry's first child entry in a plane. Available in macOS 10.1 or later.
- [copyLocation](ioregistryentry/1810296-copylocation.md)
  Returns the location string assigned to the registry entry as an OSSymbol.
- [copyName](ioregistryentry/1810315-copyname.md)
  Returns the name assigned to the registry entry as an OSSymbol.
- [copyParentEntry](ioregistryentry/1810335-copyparententry.md)
  Returns an registry entry's first parent entry in a plane. Available in macOS 10.1 or later.
- [copyProperty(const char *)](ioregistryentry/1810352-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const char *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1810371-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [copyProperty(const OSString *)](ioregistryentry/1810386-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const OSString *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1810403-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [copyProperty(const OSSymbol *)](ioregistryentry/1810428-copyproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [copyProperty(const OSSymbol *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1810451-copyproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy. Available in macOS 10.1 or later.
- [dealiasPath](ioregistryentry/1810478-dealiaspath.md)
  Strips any aliases from the head of path and returns the full path.
- [detachAbove](ioregistryentry/1810509-detachabove.md)
  Detaches an entry from all its parent entries in a plane.
- [detachAll](ioregistryentry/1810550-detachall.md)
  Detaches an entry and all its children recursively in a plane.
- [detachFromChild](ioregistryentry/1810594-detachfromchild.md)
  Detaches a child entry from its parent in a plane.
- [detachFromParent](ioregistryentry/1810632-detachfromparent.md)
  Detaches an entry from a parent entry in a plane.
- [dictionaryWithProperties](ioregistryentry/1810672-dictionarywithproperties.md)
  Synchronized method to obtain copy a registry entry's property table.
- [free](ioregistryentry/1810704-free.md)
  Standard free method for all IORegistryEntry subclasses.
- [fromPath(const char *, const IORegistryPlane *, char *, int *, IORegistryEntry *)](ioregistryentry/1810796-frompath.md)
  Looks up a registry entry by path.
- [getChildEntry](ioregistryentry/1810842-getchildentry.md)
  Returns an registry entry's first child entry in a plane.
- [getChildIterator](ioregistryentry/1810873-getchilditerator.md)
  Returns an iterator over an registry entry's child entries in a plane.
- [getDepth](ioregistryentry/1810910-getdepth.md)
  Counts the maximum number of entries between an entry and the registry root, in a plane.
- [getGenerationCount](ioregistryentry/1810941-getgenerationcount.md)
  Returns an generation count for all registry changing operations.
- [getLocation](ioregistryentry/1810970-getlocation.md)
  Returns the location string assigned to the registry entry as a C-string.
- [getName](ioregistryentry/1810990-getname.md)
  Returns the name assigned to the registry entry as a C-string.
- [getParentEntry](ioregistryentry/1811012-getparententry.md)
  Returns an registry entry's first parent entry in a plane.
- [getParentIterator](ioregistryentry/1811037-getparentiterator.md)
  Returns an iterator over an registry entry's parent entries in a specified plane.
- [getPath](ioregistryentry/1811074-getpath.md)
  Create a path for a registry entry.
- [getPathComponent](ioregistryentry/1811114-getpathcomponent.md)
  Create a path component for a registry entry.
- [getPlane](ioregistryentry/1811147-getplane.md)
  Looks up the plane object by a C-string name.
- [getProperty(const char *)](ioregistryentry/1811182-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const char *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1811215-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getProperty(const OSString *)](ioregistryentry/1811230-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const OSString *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1811244-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getProperty(const OSSymbol *)](ioregistryentry/1811254-getproperty.md)
  Synchronized method to obtain a property from a registry entry's property table.
- [getProperty(const OSSymbol *, const IORegistryPlane *, IOOptionBits)](ioregistryentry/1811263-getproperty.md)
  Synchronized method to obtain a property from a registry entry or one of its parents (or children) in the hierarchy.
- [getPropertyTable](ioregistryentry/1811272-getpropertytable.md)
  Unsynchronized accessor to a registry entry's property table.
- [getRegistryEntryID](ioregistryentry/1811281-getregistryentryid.md)
  Returns an ID for the registry entry that is global to all tasks.
- [getRegistryRoot](ioregistryentry/1811288-getregistryroot.md)
  Returns a pointer to the root instance of the registry.
- [init](ioregistryentry/1811299-init.md)
  Standard init method for all IORegistryEntry subclasses.
- [inPlane](ioregistryentry/1811307-inplane.md)
  Determines whether a registry entry is attached in a plane.
- [isChild](ioregistryentry/1811317-ischild.md)
  Determines whether a registry entry is the child of another in a plane.
- [isParent](ioregistryentry/1811327-isparent.md)
  Determines whether a registry entry is the parent of another in a plane.
- [makePlane](ioregistryentry/1811335-makeplane.md)
  Constructs an IORegistryPlane object.
- [removeProperty](ioregistryentry/1811343-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [removeProperty(const OSString *)](ioregistryentry/1811354-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [removeProperty(const OSSymbol *)](ioregistryentry/1811362-removeproperty.md)
  Synchronized method to remove a property from a registry entry's property table.
- [runPropertyAction](ioregistryentry/1811370-runpropertyaction.md)
  Single thread a call to an action w.r.t. the property lock
- [serializeProperties](ioregistryentry/1811384-serializeproperties.md)
  Synchronized method to serialize a registry entry's property table.
- [setLocation](ioregistryentry/1811397-setlocation.md)
  Sets a location string for the registry entry, in a particular plane, or globally.
- [setName(const char *, const IORegistryPlane *)](ioregistryentry/1811407-setname.md)
  Sets a name for the registry entry, in a particular plane, or globally.
- [setName(const OSSymbol *, const IORegistryPlane *)](ioregistryentry/1811420-setname.md)
  Sets a name for the registry entry, in a particular plane, or globally.
- [setProperties](ioregistryentry/1811430-setproperties.md)
  Optionally supported external method to set properties in a registry entry.
- [setProperty](ioregistryentry/1811442-setproperty.md)
  Synchronized method to construct and add an OSData property to a registry entry's property table.
- [setProperty(const char *, bool)](ioregistryentry/1811451-setproperty.md)
  Synchronized method to construct and add an OSBoolean property to a registry entry's property table.
- [setProperty(const char *, const char *)](ioregistryentry/1811461-setproperty.md)
  Synchronized method to construct and add a OSString property to a registry entry's property table.
- [setProperty(const char *, OSObject *)](ioregistryentry/1811476-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setProperty(const char *, unsigned long long, unsigned int)](ioregistryentry/1811491-setproperty.md)
  Synchronized method to construct and add an OSNumber property to a registry entry's property table.
- [setProperty(const OSString *, OSObject *)](ioregistryentry/1811507-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setProperty(const OSSymbol *, OSObject *)](ioregistryentry/1811520-setproperty.md)
  Synchronized method to add a property to a registry entry's property table.
- [setPropertyTable](ioregistryentry/1811536-setpropertytable.md)
  Replace a registry entry's property table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryentry/1810742-frompath)*
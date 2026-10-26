# errAEUnknownSendMode

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

Invalid sending mode was passed

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
errAEUnknownSendMode = -1710
```

## See Also

### Result Codes
- [noPortErr](../api-1560074-anonymous/noporterr.md)
  Client hasn’t set `'SIZE'` resource toindicate awareness of high-level events
- [destPortErr](../api-1560074-anonymous/destporterr.md)
  Server hasn’t set `'SIZE'` resource toindicate awareness of high-level events, or else is not present
- [sessClosedErr](../api-1560074-anonymous/sessclosederr.md)
  The `kAEDontReconnect` flagin the `sendMode` parameterwas set and the server quit, then restarted
- [errAECoercionFail](./erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [errAEDescNotFound](./erraedescnotfound.md)
  Descriptor was not found
- [errAECorruptData](./erraecorruptdata.md)
  Data in an Apple event could not be read
- [errAEWrongDataType](./erraewrongdatatype.md)
  Wrong descriptor type
- [errAENotAEDesc](./erraenotaedesc.md)
  Not a valid descriptor
- [errAEBadListItem](./erraebadlistitem.md)
  Operation involving a list item failed
- [errAENewerVersion](./erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [errAENotAppleEvent](./erraenotappleevent.md)
  The event is not in AppleEvent format.
- [errAEEventNotHandled](./erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [errAEReplyNotValid](./erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [errAEWaitCanceled](./erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [errAETimeout](./erraetimeout.md)
  Apple event timed out
- [errAENoUserInteraction](./erraenouserinteraction.md)
  No user interaction allowed
- [errAENotASpecialFunction](./erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [errAEParamMissed](./erraeparammissed.md)
  A required parameter was not accessed.
- [errAEUnknownAddressType](./erraeunknownaddresstype.md)
  Unknown Apple event address type
- [errAEHandlerNotFound](./erraehandlernotfound.md)
  No handler found for an Apple event
- [errAEReplyNotArrived](./erraereplynotarrived.md)
  Reply has not yet arrived
- [errAEIllegalIndex](./erraeillegalindex.md)
  Not a valid list index
- [errAEImpossibleRange](./erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [errAEWrongNumberArgs](./erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1
- [errAEAccessorNotFound](./erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [errAENoSuchLogical](./erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [errAEBadTestKey](./erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [errAENotAnObjectSpec](../../applicationservices/apple_event_manager/erraenotanobjectspec.md)
  The `objSpecifier` parameterof `AEResolve` is not anobject specifier
- [errAENoSuchObject](./erraenosuchobject.md)
  Runtime resolution of an object failed.
- [errAENegativeCount](./erraenegativecount.md)
  An object-counting function returned a negativeresult
- [errAEEmptyListContainer](./erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [errAEUnknownObjectType](./erraeunknownobjecttype.md)
  The object type isn’t recognized
- [errAERecordingIsAlreadyOn](./erraerecordingisalreadyon.md)
  Recording is already on
- [errAEReceiveTerminate](./erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [errAEReceiveEscapeCurrent](./erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [errAEEventFiltered](./erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [errAEDuplicateHandler](./erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [errAEStreamBadNesting](./erraestreambadnesting.md)
  Nesting violation while streaming
- [errAEStreamAlreadyConverted](./erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [errAEDescIsNull](./erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [errAEBuildSyntaxError](./erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [errAEBufferTooSmall](./erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [errASCantConsiderAndIgnore](../api-1559945-anonymous/errascantconsiderandignore.md)
  Can’t both consider and ignore <attribute>.
- [errASCantCompareMoreThan32k](../api-1559945-anonymous/errascantcomparemorethan32k.md)
  Can’t perform operation on text longerthan 32K bytes.
- [errASTerminologyNestingTooDeep](../api-1559945-anonymous/errasterminologynestingtoodeep.md)
  Tell statements are nested too deeply.
- [errASIllegalFormalParameter](../api-1559945-anonymous/errasillegalformalparameter.md)
  <name> is illegal as a formal parameter.
- [errASParameterNotForEvent](../api-1559945-anonymous/errasparameternotforevent.md)
  <name> is not a parameter name for the event <event>.
- [errASNoResultReturned](../api-1559945-anonymous/errasnoresultreturned.md)
  No result was returned for some argumentof this expression. 
- [errAEEventFailed](../api-1560036-anonymous/erraeeventfailed.md)
  Apple event handler failed.
- [errAETypeError](../api-1560036-anonymous/erraetypeerror.md)
  A descriptor type mismatch occurred.
- [errAEBadKeyForm](../api-1560036-anonymous/erraebadkeyform.md)
  Invalid key form.
- [errAENotModifiable](../api-1560036-anonymous/erraenotmodifiable.md)
  Can't set <object or data> to <object or data>. Access not allowed.
- [errAEPrivilegeError](../api-1560036-anonymous/erraeprivilegeerror.md)
  A privilege violation occurred.
- [errAEReadDenied](../api-1560036-anonymous/erraereaddenied.md)
  The read operation was not allowed.
- [errAEWriteDenied](../api-1560036-anonymous/erraewritedenied.md)
  Can't set <object or data> to <object or data>. 
- [errAEIndexTooLarge](../api-1560036-anonymous/erraeindextoolarge.md)
  The index of the event is too large to bevalid.
- [errAENotAnElement](../api-1560036-anonymous/erraenotanelement.md)
  The specified object is a property, notan element.
- [errAECantSupplyType](../api-1560036-anonymous/erraecantsupplytype.md)
  Can’t supply the requested descriptortype for the data.
- [errAECantHandleClass](../api-1560036-anonymous/erraecanthandleclass.md)
  The Apple event handler can’t handle objectsof this class.
- [errAEInTransaction](../api-1560036-anonymous/erraeintransaction.md)
  Couldn’t handle this command because itwasn’t part of the current transaction.
- [errAENoSuchTransaction](../api-1560036-anonymous/erraenosuchtransaction.md)
  The transaction to which this command belongedisn’t a valid transaction.
- [errAENoUserSelection](../api-1560036-anonymous/erraenouserselection.md)
  There is no user selection.
- [errAENotASingleObject](../api-1560036-anonymous/erraenotasingleobject.md)
  Handler only handles single objects.
- [errAECantUndo](../api-1560036-anonymous/erraecantundo.md)
  Can’t undo the previous Apple event oruser action.
- [errAENotAnEnumMember](../api-1560036-anonymous/erraenotanenummember.md)
  Enumerated value in `SetData` is notallowed for this property
- [errAECantPutThatThere](../api-1560036-anonymous/erraecantputthatthere.md)
  In make new, duplicate, etc. class can'tbe an element of container
- [errAEPropertiesClash](../api-1560036-anonymous/erraepropertiesclash.md)
  Illegal combination of properties settingsfor SetData, make new, or duplicate


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1560059-anonymous/erraeunknownsendmode)*
# Text Encoding Conversion Manager

**Framework**: Core Services  
**Role**: API Collection

Handle text encoding conversion between apps and transfer text across different platforms.

> **Deprecated**: Many APIs that use text encodings other than Unicode are deprecated in macOS 10. Instead, use APIs that support Unicode, such as those provided by the Foundation and Core Foundation frameworks. For more information, see [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i).

## Topics

### Result Codes
- [var kTextUnsupportedEncodingErr: Int](../ktextunsupportedencodingerr.md)
  The encoding or mapping is not supportedfor this function by the current set of tables or plug-ins.
- [var kTextMalformedInputErr: Int](../ktextmalformedinputerr.md)
  The text input contains a sequence thatis not legal in the specified encoding, such as a DBCS high byte followedby an invalid low byte (0x8120 in Shift-JIS). 
- [var kTextUndefinedElementErr: Int](../ktextundefinedelementerr.md)
  The text input contains a code point thatis undefined in the specified encoding. The function did not completelyconvert the input string. You can resume conversion from a pointbeyond the offending character, or take some other action.
- [var kTECMissingTableErr: Int](../ktecmissingtableerr.md)
  The specified encoding is partially supported,but a specific table required for this function is missing.
- [var kTECTableChecksumErr: Int](../ktectablechecksumerr.md)
  A specific table required for this functionhas a checksum error, indicating that it has become corrupted.
- [var kTECTableFormatErr: Int](../ktectableformaterr.md)
  The table format is either invalid or itcannot be handled by the current version of the code. The function didnot convert the string
- [var kTECCorruptConverterErr: Int](../kteccorruptconvertererr.md)
  The converter object is invalid. Returnedby the Text Encoding Converter functions only. 
- [var kTECNoConversionPathErr: Int](../ktecnoconversionpatherr.md)
  The converter supports both the source andtarget encodings, but cannot convert between them either directlyor indirectly. Returned by the Text Encoding Converter functionsonly. 
- [var kTECBufferBelowMinimumSizeErr: Int](../ktecbufferbelowminimumsizeerr.md)
  The output text buffer is too small to accommodatethe result of processing of the first input text element. No partof the input string was processed.
- [var kTECArrayFullErr: Int](../ktecarrayfullerr.md)
- [var kTECPartialCharErr: Int](../ktecpartialcharerr.md)
  The input text ends in the middle of a multibytecharacter and conversion stopped. Append the unconverted input fromthis call to the beginning of the subsequent input text and callthe function again.
- [var kTECUnmappableElementErr: Int](../ktecunmappableelementerr.md)
  An input text element cannot be mapped tothe specified output encoding(s) using the specified options. Forthe Unicode Converter, this error can occur only if kUnicodeUseFallbacksBitcontrol flag is not set. 
- [var kTECIncompleteElementErr: Int](../ktecincompleteelementerr.md)
  The input text ends with a text elementthat might be incomplete, or contains a text element that is too longfor the internal buffers. 
- [var kTECDirectionErr: Int](../ktecdirectionerr.md)
  An error, such as a direction stack overflow,occurred in directionality processing.
- [var kTECGlobalsUnavailableErr: Int](../ktecglobalsunavailableerr.md)
  Global variables have already been deallocated,premature termination. The function did not convert the string.
- [var kTECItemUnavailableErr: Int](../ktecitemunavailableerr.md)
  An item (for example, a name) is not availablefor the specified region (and encoding, if relevant).
- [var kTECUsedFallbacksStatus: Int](../ktecusedfallbacksstatus.md)
  The function has completely converted theinput string to the specified target using one or more fallbacks.For the Unicode Converter, this status code can only occur if the `kUnicodeUseFallbacksBit`control flag is set.
- [var kTECNeedFlushStatus: Int](../ktecneedflushstatus.md)
  The application disposed of a converterobject by calling TECDisposeConverter, but there is still text containedin internal buffers. Returned by the Text Encoding Converter functionsonly. 
- [var kTECOutputBufferFullStatus: Int](../ktecoutputbufferfullstatus.md)
  The converter successfully converted partof the input text, but the output buffer was not large enough toaccommodate the entire input text after conversion. Convert theremaining text beginning from the position where the conversion stopped. 
- [kTextUnsupportedEncodingErr](../api-1560006-anonymous/ktextunsupportedencodingerr.md)
  The encoding or mapping is not supportedfor this function by the current set of tables or plug-ins.
- [kTextMalformedInputErr](../api-1560006-anonymous/ktextmalformedinputerr.md)
  The text input contains a sequence thatis not legal in the specified encoding, such as a DBCS high byte followedby an invalid low byte (0x8120 in Shift-JIS). 
- [kTextUndefinedElementErr](../api-1560006-anonymous/ktextundefinedelementerr.md)
  The text input contains a code point thatis undefined in the specified encoding. The function did not completelyconvert the input string. You can resume conversion from a pointbeyond the offending character, or take some other action.
- [kTECMissingTableErr](../api-1560006-anonymous/ktecmissingtableerr.md)
  The specified encoding is partially supported,but a specific table required for this function is missing.
- [kTECTableChecksumErr](../api-1560006-anonymous/ktectablechecksumerr.md)
  A specific table required for this functionhas a checksum error, indicating that it has become corrupted.
- [kTECTableFormatErr](../api-1560006-anonymous/ktectableformaterr.md)
  The table format is either invalid or itcannot be handled by the current version of the code. The function didnot convert the string
- [kTECCorruptConverterErr](../api-1560006-anonymous/kteccorruptconvertererr.md)
  The converter object is invalid. Returnedby the Text Encoding Converter functions only. 
- [kTECNoConversionPathErr](../api-1560006-anonymous/ktecnoconversionpatherr.md)
  The converter supports both the source andtarget encodings, but cannot convert between them either directlyor indirectly. Returned by the Text Encoding Converter functionsonly. 
- [kTECBufferBelowMinimumSizeErr](../api-1560006-anonymous/ktecbufferbelowminimumsizeerr.md)
  The output text buffer is too small to accommodatethe result of processing of the first input text element. No partof the input string was processed.
- [kTECArrayFullErr](../api-1560006-anonymous/ktecarrayfullerr.md)
- [kTECPartialCharErr](../api-1560006-anonymous/ktecpartialcharerr.md)
  The input text ends in the middle of a multibytecharacter and conversion stopped. Append the unconverted input fromthis call to the beginning of the subsequent input text and callthe function again.
- [kTECUnmappableElementErr](../api-1560006-anonymous/ktecunmappableelementerr.md)
  An input text element cannot be mapped tothe specified output encoding(s) using the specified options. Forthe Unicode Converter, this error can occur only if kUnicodeUseFallbacksBitcontrol flag is not set. 
- [kTECIncompleteElementErr](../api-1560006-anonymous/ktecincompleteelementerr.md)
  The input text ends with a text elementthat might be incomplete, or contains a text element that is too longfor the internal buffers. 
- [kTECDirectionErr](../api-1560006-anonymous/ktecdirectionerr.md)
  An error, such as a direction stack overflow,occurred in directionality processing.
- [kTECGlobalsUnavailableErr](../api-1560006-anonymous/ktecglobalsunavailableerr.md)
  Global variables have already been deallocated,premature termination. The function did not convert the string.
- [kTECItemUnavailableErr](../api-1560006-anonymous/ktecitemunavailableerr.md)
  An item (for example, a name) is not availablefor the specified region (and encoding, if relevant).
- [kTECUsedFallbacksStatus](../api-1560006-anonymous/ktecusedfallbacksstatus.md)
  The function has completely converted theinput string to the specified target using one or more fallbacks.For the Unicode Converter, this status code can only occur if the `kUnicodeUseFallbacksBit`control flag is set.
- [kTECNeedFlushStatus](../api-1560006-anonymous/ktecneedflushstatus.md)
  The application disposed of a converterobject by calling TECDisposeConverter, but there is still text containedin internal buffers. Returned by the Text Encoding Converter functionsonly. 
- [kTECOutputBufferFullStatus](../api-1560006-anonymous/ktecoutputbufferfullstatus.md)
  The converter successfully converted partof the input text, but the output buffer was not large enough toaccommodate the entire input text after conversion. Convert theremaining text beginning from the position where the conversion stopped. 
### Creating a Text Encoding Specification
- [CreateTextEncoding](../api-1399639-createtextencoding.md)
  Creates and returns a text encoding specification.
### Obtaining Information From a Text Encoding Specification
- [GetTextEncodingBase](../api-1399792-gettextencodingbase.md)
  Returns the base encoding of the specified text encoding. 
- [GetTextEncodingFormat](../api-1400318-gettextencodingformat.md)
  Returns the format value of the specified text encoding. 
- [GetTextEncodingName](../api-1399645-gettextencodingname.md)
  Returns the localized name for a specified text encoding. 
- [GetTextEncodingVariant](../api-1400250-gettextencodingvariant.md)
  Returns the variant from the specified text encoding. 
- [ResolveDefaultTextEncoding](../api-1400111-resolvedefaulttextencoding.md)
  Returns a text encoding specification in which any meta-valueshave been resolved to real values. Currently, this affects onlythe base encoding values packed into the text encoding specification. 
### Converting Between Script Manager Values and Text Encodings
- [RevertTextEncodingToScriptInfo](../api-1400023-reverttextencodingtoscriptinfo.md)
  Converts the given Mac OS text encoding specificationto the corresponding script code and, if possible, language codeand font name.
- [UpgradeScriptInfoToTextEncoding](../api-1399625-upgradescriptinfototextencoding.md)
  Converts any combination of a Mac OS script code, a languagecode, a region code, and a font name to a text encoding.
### Obtaining Information About Available Text Encodings
- [TECCountAvailableTextEncodings](../api-1571853-teccountavailabletextencodings.md)
  Counts and returns the number of text encodings currentlyconfigured in the Text Encoding Converter.
- [TECCountSubTextEncodings](../api-1571820-teccountsubtextencodings.md)
  Counts and returns the number of subencodings a text encodingsupports.
- [TECGetAvailableTextEncodings](../api-1571819-tecgetavailabletextencodings.md)
  Returns the text encoding specifications currently configuredin the Text Encoding Converter.
- [TECGetSubTextEncodings](../api-1571796-tecgetsubtextencodings.md)
  Returns the text encoding specifications for the subencodingsthe encoding scheme supports. 
- [NearestMacTextEncodings](../api-1399736-nearestmactextencodings.md)
  Obtains the best and alternate Mac text encoding.
### Identifying Direct Encoding Conversions 
- [TECCountDirectTextEncodingConversions](../api-1571822-teccountdirecttextencodingconver.md)
  Counts and returns the number of direct conversions currentlyconfigured in the Text Encoding Converter.
- [TECGetDirectTextEncodingConversions](../api-1571834-tecgetdirecttextencodingconversi.md)
  Returns the types of direct conversions currently configuredin the Text Encoding Converter.
### Identifying Possible Destination Encodings
- [TECCountDestinationTextEncodings](../api-1571805-teccountdestinationtextencodings.md)
  Counts and returns the number of destination encodingsto which a specified source encoding can be converted in one step.
- [TECGetDestinationTextEncodings](../api-1571808-tecgetdestinationtextencodings.md)
  Returns the encoding specifications for all the destinationtext encodings to which the Text Encoding Converter can directlyconvert the specified source encoding.
### Obtaining Converter Information
- [TECGetInfo](../api-1400430-tecgetinfo.md)
  Allocates a converter information structure of type `TECInfo` inthe application heap using `NewHandle`,fills it out, and returns a handle. 
### Creating and Deleting Converter Objects
- [TECCreateConverter](../api-1571815-teccreateconverter.md)
  Determines a conversion path for a source and destinationencoding, then creates a text encoding converter object and returnsa pointer to it. 
- [TECCreateConverterFromPath](../api-1571829-teccreateconverterfrompath.md)
  Creates a converter object for a specific conversion path—froma source encoding through intermediate encodings to a destinationencoding—and returns a pointer to it. 
- [TECClearConverterContextInfo](../api-1571844-tecclearconvertercontextinfo.md)
  Resets a converter object to its initial state so youcan reuse it. 
- [TECDisposeConverter](../api-1571839-tecdisposeconverter.md)
  Disposes of a converter object.
### Converting Text Between Encodings
- [TECConvertText](../api-1571824-tecconverttext.md)
  Converts a stream of text from a source encoding to adestination encoding. It uses the conversion path specified by theconverter object you supply.
- [TECFlushText](../api-1571848-tecflushtext.md)
  Flushes out any data in a converter object’s temporarybuffers and resets the converter object.
### Converting to Multiple Encoding Runs
- [TECConvertTextToMultipleEncodings](../api-1571849-tecconverttexttomultipleencoding.md)
  Converts text in the source encoding to runs of text inmultiple destination encodings. It uses the conversion path specifiedin the converter object you supply.
- [TECCreateOneToManyConverter](../api-1571794-teccreateonetomanyconverter.md)
  Determines a conversion path for the source encoding anddestinations encodings you specify, creates a text encoding converterobject, and returns a reference to it. 
- [TECFlushMultipleEncodings](../api-1571842-tecflushmultipleencodings.md)
  Flushes out any encodings that may be stored in a converterobject’s temporary buffers and shifts encodings back to theirdefault state, if any.
- [TECGetEncodingList](../api-1571830-tecgetencodinglist.md)
  Gets the list of destination encodings from a converterobject.
### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](../api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECClearSnifferContextInfo](../api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECDisposeSniffer](../api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECCountAvailableSniffers](../api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECGetAvailableSniffers](../api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.
- [TECSniffTextEncoding](../api-1571836-tecsnifftextencoding.md)
  Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 
### Getting Information About Internet and Regional Text Encoding Names
- [TECCountMailTextEncodings](../api-1571826-teccountmailtextencodings.md)
  Counts and returns the number of currently supported e-mailencodings for a specified region.
- [TECCountWebTextEncodings](../api-1571837-teccountwebtextencodings.md)
  Counts and returns the number of currently supported textencodings for a region code. 
- [TECGetMailTextEncodings](../api-1571845-tecgetmailtextencodings.md)
  Returns the currently supported mail encoding specificationsfor a region code. 
- [TECGetTextEncodingFromInternetName](../api-1571825-tecgettextencodingfrominternetna.md)
  Returns the Mac OS text encoding specification that correspondsto an Internet encoding name.
- [TECGetTextEncodingInternetName](../api-1571851-tecgettextencodinginternetname.md)
  Returns the Internet encoding name that corresponds toa Mac OS text encoding. 
- [TECGetWebTextEncodings](../api-1571798-tecgetwebtextencodings.md)
  Returns the currently supported text encoding specificationsfor a region code.
### Converting to Unicode
- [ChangeTextToUnicodeInfo](../api-1433487-changetexttounicodeinfo.md)
  Changes the mapping information for the specified Unicodeconverter object used to convert text to Unicode to the new mappingyou provide. 
- [ConvertFromTextToUnicode](../api-1433517-convertfromtexttounicode.md)
  Converts a string from any encoding to Unicode. 
- [CreateTextToUnicodeInfo](../api-1433598-createtexttounicodeinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from a non-Unicode encodingto Unicode. 
- [CreateTextToUnicodeInfoByEncoding](../api-1433560-createtexttounicodeinfobyencodin.md)
  Based on the given text encoding specification, createsand returns a Unicode converter object containing information requiredfor converting strings from the specified non-Unicode encoding toUnicode. 
- [DisposeTextToUnicodeInfo](../api-1433669-disposetexttounicodeinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetTextToUnicodeInfo](../api-1433526-resettexttounicodeinfo.md)
  Reinitializes all state information kept by the contextobjects.
### Converting From Unicode
- [ChangeUnicodeToTextInfo](../api-1433509-changeunicodetotextinfo.md)
  Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 
- [ConvertFromUnicodeToText](../api-1433542-convertfromunicodetotext.md)
  Converts a Unicode text string to the destination encodingyou specify. 
- [CreateUnicodeToTextInfo](../api-1433522-createunicodetotextinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 
- [CreateUnicodeToTextInfoByEncoding](../api-1433550-createunicodetotextinfobyencodin.md)
  Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.
- [DisposeUnicodeToTextInfo](../api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextInfo](../api-1433647-resetunicodetotextinfo.md)
  Reinitializes all state information kept by a Unicodeconverter object.
### Converting From Unicode to Multiple Encodings
- [ConvertFromUnicodeToTextRun](../api-1433511-convertfromunicodetotextrun.md)
  Converts a string from Unicode to one or more encodings. 
- [ConvertFromUnicodeToScriptCodeRun](../api-1433662-convertfromunicodetoscriptcoderu.md)
  Converts a string from Unicode to one or more scripts. 
- [CreateUnicodeToTextRunInfo](../api-1433632-createunicodetotextruninfo.md)
  Creates and returns a Unicode converter object containingthe information required for converting a Unicode text string tostrings in one or more non-Unicode encodings. 
- [CreateUnicodeToTextRunInfoByEncoding](../api-1433651-createunicodetotextruninfobyenco.md)
  Based on the given text encoding specifications for theconverted text runs, creates and returns a Unicode converter objectcontaining information required for converting strings from Unicodeto one or more specified non-Unicode encodings.
- [CreateUnicodeToTextRunInfoByScriptCode](../api-1433657-createunicodetotextruninfobyscri.md)
  Based on the given script codes for the converted textruns, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to oneor more specified non-Unicode encodings.
- [DisposeUnicodeToTextRunInfo](../api-1433595-disposeunicodetotextruninfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextRunInfo](../api-1433495-resetunicodetotextruninfo.md)
  Reinitializes all state information kept by the contextobjects in TextRun conversions.
### Converting Between Unicode and Pascal Strings
- [ConvertFromPStringToUnicode](../api-1433483-convertfrompstringtounicode.md)
  Converts a Pascal string in a Mac OS text encoding toa Unicode string. 
- [ConvertFromUnicodeToPString](../api-1433581-convertfromunicodetopstring.md)
  Converts a Unicode string to Pascal in a Mac OS text encoding. 
### Obtaining Unicode Mapping Information 
- [CountUnicodeMappings](../api-1433665-countunicodemappings.md)
  Counts available mappings that meet the specified matchingcriteria.
- [QueryUnicodeMappings](../api-1433630-queryunicodemappings.md)
  Returns a list of the conversion mappings available onthe system that meet specified matching criteria and returns thenumber of mappings found. 
### Truncating Strings Before Converting Them 
- [TruncateForTextToUnicode](../api-1433518-truncatefortexttounicode.md)
  Identifies where your application can safely break a multibytestring to be converted to Unicode so that the string is not brokenin the middle of a multibyte character. 
- [TruncateForUnicodeToText](../api-1433649-truncateforunicodetotext.md)
  Identifies where your application can safely break a Unicodestring to be converted to any encoding so that the string is brokenin a way that preserves the text element integrity. 
### Setting the Fallback Handler
- [SetFallbackUnicodeToText](../api-1433614-setfallbackunicodetotext.md)
  Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by theUnicode converter object.
- [SetFallbackUnicodeToTextRun](../api-1433644-setfallbackunicodetotextrun.md)
  Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by a Unicodeconverter object.
### Working With Universal Procedure Pointers
- [NewUnicodeToTextFallbackUPP](../api-1433556-newunicodetotextfallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a Unicode-to-textfallback callback.
- [DisposeUnicodeToTextFallbackUPP](../api-1433648-disposeunicodetotextfallbackupp.md)
  Disposes of a a new universal procedure pointer (UPP)to a Unicode-to-text fallback callback.
- [InvokeUnicodeToTextFallbackUPP](../api-1433599-invokeunicodetotextfallbackupp.md)
  Calls your Unicode-to-text fallback callback.
### Getting UniChar Property Values
- [UCGetCharProperty](../api-1400224-ucgetcharproperty.md)
  Obtains the value associated with a property type forthe specified `UniChar` characters.
### Callbacks
- [UnicodeToTextFallbackProcPtr](../unicodetotextfallbackprocptr.md)
  Defines a pointer to a function that convertsa Unicode text element for which there is no destination encodingequivalent in the appropriate mapping table to the fallback character sequencedefined by your fallback handler, and returns the converted charactersequence to the Unicode Converter.
- [TECPluginGetPluginDispatchTablePtr](../tecplugingetplugindispatchtableptr.md)
  Defines a pointer to a function that returnsa pointer to a plug-in dispatch table.
- [TECPluginNewEncodingConverterPtr](../tecpluginnewencodingconverterptr.md)
  Defines a pointer to a function that determinesa conversion path for a source and destination encoding, then createsa text encoding converter object and returns a pointer to it.
- [TECPluginClearContextInfoPtr](../tecpluginclearcontextinfoptr.md)
  Defines a pointer to a function that resets aconverter object to its initial state.
- [TECPluginConvertTextEncodingPtr](../tecpluginconverttextencodingptr.md)
  Defines a pointer to a function that convertsstream of text from a source encoding to a destination encoding,using the conversion path specified by the converter object you supply.
- [TECPluginFlushConversionPtr](../tecpluginflushconversionptr.md)
  Defines a pointer to a function that flushesout any data in a converter object’s temporary buffers and resetsthe converter object.
- [TECPluginDisposeEncodingConverterPtr](../tecplugindisposeencodingconverterptr.md)
  Defines a pointer to a function that disposesof a converter object.
- [TECPluginNewEncodingSnifferPtr](../tecpluginnewencodingsnifferptr.md)
  Defines a pointer to a function that createsa sniffer object and returns a reference to it.
- [TECPluginClearSnifferContextInfoPtr](../tecpluginclearsniffercontextinfoptr.md)
  Defines a pointer to a function that resets asniffer object to its initial settings.
- [TECPluginSniffTextEncodingPtr](../tecpluginsnifftextencodingptr.md)
  Defines a pointer toa function that analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply;it also returns the number of errors and features for each encoding. 
- [TECPluginDisposeEncodingSnifferPtr](../tecplugindisposeencodingsnifferptr.md)
  Defines a pointer to a function that disposesof a sniffer object.
- [TECPluginGetCountAvailableTextEncodingsPtr](../tecplugingetcountavailabletextencodingsptr.md)
  Defines a pointer to a function that obtainsthe available text encodings.
- [TECPluginGetCountAvailableTextEncodingPairsPtr](../tecplugingetcountavailabletextencodingpairsptr.md)
  Defines a pointer to a function that obtainsthe available text encoding pairs.
- [TECPluginGetCountDestinationTextEncodingsPtr](../tecplugingetcountdestinationtextencodingsptr.md)
  Defines a pointer to a function that counts andreturns the number of destination encodings to which a specifiedsource encoding can be converted in one step.
- [TECPluginGetCountSubTextEncodingsPtr](../tecplugingetcountsubtextencodingsptr.md)
  Defines a pointer to a function that obtainsthe text encoding specifications for the subencodings the encodingscheme supports.
- [TECPluginGetCountAvailableSniffersPtr](../tecplugingetcountavailablesniffersptr.md)
  Defines a pointer to a function that counts andreturns the number of sniffers available in all installed plug-ins.
- [TECPluginGetCountWebEncodingsPtr](../tecplugingetcountwebencodingsptr.md)
  Defines a pointer to a function that obtainsthe available web text encodings.
- [TECPluginGetCountMailEncodingsPtr](../tecplugingetcountmailencodingsptr.md)
  Defines a pointer to a function that obtainsthe text encodings available for email.
- [TECPluginGetTextEncodingInternetNamePtr](../tecplugingettextencodinginternetnameptr.md)
  Defines a pointer to a function that obtainsthe Internet text encoding name for a text encoding specification.
- [TECPluginGetTextEncodingFromInternetNamePtr](../tecplugingettextencodingfrominternetnameptr.md)
  Defines a pointer to a function that obtainsthe text encoding for an Internet text encoding name.
### Structures
- [TECEncodingPairRec](../tecencodingpairrec.md)
- [TECEncodingPairs](../tecencodingpairs.md)
- [TECEncodingPairsRec](../tecencodingpairsrec.md)
- [TECEncodingsListRec](../tecencodingslistrec.md)
- [TECInternetNameRec](../tecinternetnamerec.md)
- [TECInternetNamesRec](../tecinternetnamesrec.md)
- [TECLocaleListToEncodingListRec](../teclocalelisttoencodinglistrec.md)
- [TECLocaleToEncodingsListRec](../teclocaletoencodingslistrec.md)
- [TECSubTextEncodingRec](../tecsubtextencodingrec.md)
- [TECSubTextEncodingsRec](../tecsubtextencodingsrec.md)
### Data Types
- [ConstScriptCodeRunPtr](../constscriptcoderunptr.md)
  Defines a constant script code run pointer.
- [ConstTextEncodingRunPtr](../consttextencodingrunptr.md)
  Defines a constant text encoding run pointer.
- [ConstTextPtr](../consttextptr.md)
  Defines a constant text pointer.
- [ConstTextToUnicodeInfo](../consttexttounicodeinfo.md)
  Defines a constant text to Unicode converter object.
- [ConstUniCharArrayPtr](../constunichararrayptr.md)
  Defines a constant Unicode character array pointer.
- [ConstUnicodeMappingPtr](../constunicodemappingptr.md)
  Defines a constant Unicode mapping pointer.
- [ConstUnicodeToTextInfo](../constunicodetotextinfo.md)
  Defines a constant Unicode to text converter object.
- [ScriptCodeRun](../scriptcoderun.md)
  Contains script code information for a text run.
- [TECBufferContextRec](../tecbuffercontextrec.md)
  Contains buffers for text and text encoding runs.
- [TECConversionInfo](../tecconversioninfo.md)
  Contains text encoding conversion information.
- [TECConverterContextRec](../tecconvertercontextrec.md)
  Contains converter information used by a Text Encoding Converter plug-in.
- [TECInfo](../tecinfo.md)
  Contains information about the Unicode Converter, the Text Encoding Converter, and Basic Text Types.
- [TECObjectRef](../tecobjectref.md)
  Defines an opaque reference to a converter object.
- [TECPluginDispatchTable](../tecplugindispatchtable.md)
  Contains version and signature information and pointers to the callback functions used by a text encoding converter plug-in.
- [TECPluginSig](../tecpluginsig.md)
  Defines a data type for a Text Encoding Converter plug-in signature.
- [TECPluginSignature](../tecpluginsignature.md)
  Defines a data type for a Text Encoding Converter plug-in signature.
- [TECPluginStateRec](../tecpluginstaterec.md)
  Contains state information for a Text Encoding Converter plug-in.
- [TECPluginVersion](../tecpluginversion.md)
  Defines a data type for Text Encoding Converter plug-in version.
- [TECSnifferContextRec](../tecsniffercontextrec.md)
  Contains infomation used by a sniffer object.
- [TECSnifferObjectRef](../tecsnifferobjectref.md)
  Defines a reference to an opaque sniffer object.
- [TextEncoding](../textencoding.md)
  Defines a data type for a text encoding value.
- [TextEncodingRun](../textencodingrun.md)
  Contains text encoding information for a text run.
- [TextEncodingVariant](../textencodingvariant.md)
  Defines a data type for a text encoding variant. 
- [TextToUnicodeInfo](../texttounicodeinfo.md)
  Defines reference to an opaque Unicode converter object.
- [UniCharArrayOffset](../unichararrayoffset.md)
  Represents the boundary between two characters.
- [UnicodeMapping](../unicodemapping.md)
  Contains information for mapping to or from Unicode encoding.
- [UnicodeToTextFallbackUPP](../unicodetotextfallbackupp.md)
  Defines a universal procedure pointer to a Unicode-to-text-fallback callback function.
- [UnicodeToTextInfo](../unicodetotextinfo.md)
  Defines a reference to an opaque Unicode to text converter object.
- [UnicodeToTextRunInfo](../unicodetotextruninfo.md)
  Defines a reference to an opaque Unicode to text run information converter object.
- [TECEncodingPairsHandle](../tecencodingpairshandle.md)
- [TECEncodingPairsPtr](../tecencodingpairsptr.md)
- [TECEncodingsListHandle](../tecencodingslisthandle.md)
- [TECEncodingsListPtr](../tecencodingslistptr.md)
- [TECInfoHandle](../tecinfohandle.md)
- [TECInfoPtr](../tecinfoptr.md)
- [TECInternetNameUsageMask](../tecinternetnameusagemask.md)
- [TECInternetNamesHandle](../tecinternetnameshandle.md)
- [TECInternetNamesPtr](../tecinternetnamesptr.md)
- [TECLocaleListToEncodingListPtr](../teclocalelisttoencodinglistptr.md)
- [TECLocaleToEncodingsListHandle](../teclocaletoencodingslisthandle.md)
- [TECLocaleToEncodingsListPtr](../teclocaletoencodingslistptr.md)
- [TECSubTextEncodingsHandle](../tecsubtextencodingshandle.md)
- [TECSubTextEncodingsPtr](../tecsubtextencodingsptr.md)
### Feature Selectors
- [Conversion Flags](../api-1433583-conversion_flags.md)
  Specify how to perform conversion of text from one encoding to another.
- [Conversion Masks](../api-1433493-conversion_masks.md)
  Set or text for conversion flags.
- [Directionality Flags](../api-1433491-directionality_flags.md)
  Specify a text direction.
- [Directionality Masks](../api-1433620-directionality_masks.md)
  Set or text for directionality bits.
- [Unicode Converter Flags](../api-1400304-unicode_converter_flags.md)
  Specify features for bug fixes in the Unicode Converter.
- [Unicode Converter Masks](../api-1400367-unicode_converter_masks.md)
  Set or test for Unicode converter flags.
- [Unicode Fallback Sequencing Flag](../api-1433597-unicode_fallback_sequencing_flag.md)
  Specifies options for setting fallback sequencing.
- [Unicode Fallback Sequencing Masks](../api-1433622-unicode_fallback_sequencing_mask.md)
  Set or text for Unicode sequencing flag.
- [Unicode Matching Flags](../api-1433572-unicode_matching_flags.md)
  Specify matching criteria for Unicode mappings. 
- [Unicode Matching Masks](../api-1433554-unicode_matching_masks.md)
  Used to set or test for Unicode matching flags.
- [Fallback Handler Selectors](../api-1433507-fallback_handler_selectors.md)
  Specify a fallback handler for the Unicode Converter to use.
### Encodings and Variants
- [TextEncodingBase](../textencodingbase.md)
  Specify base text encodings.
- [Compatibility TextEncodings](../api-1399939-compatibility_textencodings.md)
  Specify text encodings that are provided for backward compatibility.
- [EBCDIC and IBM Host Text Encodings](../api-1400244-ebcdic_and_ibm_host_text_encodin.md)
  Specify text encodings used by IBM computers.
- [Encoding Variants for Big-5](../api-1399673-encoding_variants_for_big-5.md)
  Specify variants of Big-5 encoding.
- [Encoding Variants for Mac OS Encodings](../api-1399862-encoding_variants_for_mac_os_enc.md)
  Specify variant Mac OS encodings that use script codes other than 0
- [Encoding Variants for MacArabic](../api-1399984-encoding_variants_for_macarabic.md)
  Specify variants of MacArabic.
- [Encoding Variants for MacCroatian](../api-1400365-encoding_variants_for_maccroatia.md)
  Specify variants of MacCroation.
- [Encoding Variants for MacCyrillic](../api-1400107-encoding_variants_for_maccyrilli.md)
  Specify variants of MacCyrillic.
- [Encoding Variants for MacFarsi](../api-1399681-encoding_variants_for_macfarsi.md)
  Specify variants of MacFarsi.
- [Encoding Variants for MacHebrew](../api-1400410-encoding_variants_for_machebrew.md)
  Specify variants of MacHebrew.
- [Encoding Variants for MacIcelandic](../api-1400089-encoding_variants_for_maciceland.md)
  Specify variants of MacIcelandic.
- [Encoding Variants for MacJapanese](../api-1399915-encoding_variants_for_macjapanes.md)
  Specify variants of MacJapanese.
- [Encoding Variants for MacRoman](../api-1399701-encoding_variants_for_macroman.md)
  Specify variants of MacRoman.
- [Encoding Variants for MacRoman Related to Currency](../api-1399860-encoding_variants_for_macroman_r.md)
  Specify variants of MacRoman that are related to currency.
- [Encoding Variants for MacRomanian](../api-1399955-encoding_variants_for_macromania.md)
  Specify variants of MacRomanian.
- [Encoding Variants for MacRomanLatin1](../api-1400256-encoding_variants_for_macromanla.md)
  Specify variants of MacRomanLatin1.
- [Encoding Variants for MacVT100](../api-1400045-encoding_variants_for_macvt100.md)
  Specify variants of MacVT100.
- [Encoding Variants for Unicode](../api-1399897-encoding_variants_for_unicode.md)
  Specify variants of Unicode.
- [EUC Text Encodings](../api-1399707-euc_text_encodings.md)
  Specify Extendec Unix Code text encodings.
- [HFS Text Encoding](../api-1400242-hfs_text_encoding.md)
  Specifies a Mac OS HFS text encoding.
- [ISO 2022 Text Encodings](../api-1400073-iso_2022_text_encodings.md)
  Specify text encodings for ISO 2002.
- [ISO 8-bit and 7-bit Text Encodings](../api-1399699-iso_8-bit_and_7-bit_text_encodings.md)
  Specify text encodings for ISO 8-bit and 7-bit.
- [Mac Unicode Text Encoding](../api-1399907-mac_unicode_text_encoding.md)
  Specifies a script code that should be handled as a special Mac OS script code.
- [Miscellaneous Text Encoding Standards](../api-1399782-miscellaneous_text_encoding_stan.md)
  Specify miscellaneous text encodings.
- [MS-DOS and Windows Text Encodings](../api-1400434-ms-dos_and_windows_text_encodings.md)
  Specify text encodings for MS-DOS and Windows.
- [National Standard Text Encodings](../api-1400246-national_standard_text_encodings.md)
  Specify text encodings for various national standards.
- [NextStep Platform Encodings](../api-1400238-nextstep_platform_encodings.md)
  Specify text encodings for the NextStep platform.
- [Special Text Encoding Values](../api-1400396-special_text_encoding_values.md)
  Specify special cases of text encodings.
- [TextEncodingFormat](../textencodingformat.md)
  Specify a text encoding format.
- [TextEncodingNameSelector](../textencodingnameselector.md)
  Specify the part of an encoding name you want to obtain.
- [Text Encoding Variants](../api-1400145-text_encoding_variants.md)
  Specify minor variants of a base encoding or group of base encodings.
- [Unicode and ISO UCS Text Encodings](../api-1400188-unicode_and_iso_ucs_text_encodin.md)
  Specify Unicode and IOS UCS text encodings.
- [Unsupported Unicode Variants](../api-1400371-unsupported_unicode_variants.md)
  Represent Unicode variants that are not yet supported or fully defined.
### Assorted Constants
- [Bidirectional Character Values](../api-1400035-bidirectional_character_values.md)
  Specify bidirectional character properties.
- [Common and Special Unicode Values](../api-1400154-common_and_special_unicode_value.md)
  Specify sommon and special Unicode code values.
- [TEC Plugin Dispatch Table Versions](../api-1498348-tec_plugin_dispatch_table_versio.md)
  Specify a version for a TEC plug-in dispatch table.
- [TEC Plug-in Signatures](../api-1571831-tec_plug-in_signatures.md)
  Specify a TEC plug-in signature.
- [UCCharPropertyType](../uccharpropertytype.md)
  Specify property types for a Unicode charater.
- [UCCharPropertyValue](../uccharpropertyvalue.md)
  Specify a propery value for a Unicode character.
- [UnicodeMapVersion](../unicodemapversion.md)
  Specify a Unicode mapping version.
- [Unwanted Data Constants](../api-1400314-unwanted_data_constants.md)
  Specify data you don’t care about receiving.

## See Also

### Managers
- [Component Manager](./component_manager.md)
  Find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. 
- [Gestalt Manager](./gestalt_manager.md)
  Investigate the operating environment of your app.
- [Alias Manager](./alias_manager.md)
  Create and resolve alias records that describe file system objects such as files, directories, and volumes. 
- [File Manager](./file_manager.md)
  Interact with files, folders, and volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/text_encoding_conversion_manager)*
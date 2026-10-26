# Search Kit

**Framework**: Core Services  
**Role**: API Collection

Index and search natural language documents.

#### Overview

Search Kit is a powerful and streamlined C language framework for indexing and searching text in most human languages. It provides fast information retrieval in System Preferences, Address Book, Help Viewer, and Xcode. Apple’s Spotlight technology is built on top of Search Kit to provide content searching in Finder, Mail, and the Spotlight menu. 

You can use Search Kit or Spotlight to provide similar functionality and powerful information-access capabilities within your Mac OS X application. The Search Kit API is appropriate when you want your application to have full control over indexing and searching, and when your focus is file content. Search Kit is thread-safe and works with Cocoa, Carbon, and command-line tools. 

Beginning with Mac OS X version 10.4, Search Kit supports phrase searches, prefix/suffix/substring searches, improved Boolean searches, and improved relevance ranking. Search Kit now uses Spotlight’s metadata importers when indexing documents, and takes advantage of any additional importers available on a system. Searching and indexing are much faster with Search Kit’s new asynchronous search APIs. And, starting in Mac OS X v10.4, Search Kit provides a summarization API that supplants Find By Content.

##### Overview

Search Kit is a powerful and streamlined C language framework for indexing and searching text in most human languages. It provides fast information retrieval in System Preferences, Address Book, Help Viewer, and Xcode. Apple’s Spotlight technology is built on top of Search Kit to provide content searching in Finder, Mail, and the Spotlight menu.

You can use Search Kit or Spotlight to provide similar functionality and powerful information-access capabilities within your Mac app. Search Kit is appropriate when you want your application to have full control over indexing and searching, and when your focus is file content. Search Kit is thread-safe and works with Cocoa and command-line tools.

Search Kit supports phrase searches, prefix/suffix/substring searches, Boolean searches, summarization, and relevance ranking. Search Kit uses Spotlight’s metadata importers when indexing documents and takes advantage of any additional importers available on a system. 

## Topics

### Creating, Opening, and Closing Indexes
- [func SKIndexCreateWithURL(CFURL!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](./api-1446111-skindexcreatewithurl.md)
  Creates a named index in a file whose location is specified with a CFURL object.
- [func SKIndexCreateWithMutableData(CFMutableData!, CFString!, SKIndexType, CFDictionary!) -> Unmanaged<SKIndex>!](./api-1447500-skindexcreatewithmutabledata.md)
  Creates a named index stored in a `CFMutableDataRef` object.
- [func SKIndexOpenWithData(CFData!, CFString!) -> Unmanaged<SKIndex>!](./api-1446398-skindexopenwithdata.md)
  Opens an existing, named index for searching only.
- [func SKIndexOpenWithMutableData(CFMutableData!, CFString!) -> Unmanaged<SKIndex>!](./api-1444201-skindexopenwithmutabledata.md)
  Opens an existing, named index for searching and updating.
- [func SKIndexOpenWithURL(CFURL!, CFString!, Bool) -> Unmanaged<SKIndex>!](./api-1449017-skindexopenwithurl.md)
  Opens an existing, named index stored in a file whose location is specified with a CFURL object.
- [func SKIndexClose(SKIndex!)](./api-1442401-skindexclose.md)
  Closes an index.
- [func SKIndexGetIndexType(SKIndex!) -> SKIndexType](./api-1442236-skindexgetindextype.md)
  Gets the category of an index.
- [func SKIndexGetTypeID() -> CFTypeID](./api-1450223-skindexgettypeid.md)
  Gets the type identifier for Search Kit indexes.
### Managing Indexes
- [func SKIndexAddDocumentWithText(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](./api-1444518-skindexadddocumentwithtext.md)
  Adds a document URL ([`SKDocument`](./skdocument.md)) object, and the associated document’s textual content, to an index.
- [func SKIndexAddDocument(SKIndex!, SKDocument!, CFString!, Bool) -> Bool](./api-1444897-skindexadddocument.md)
  Adds location information for a file-based document, and the document’s textual content, to an index.
- [func SKIndexFlush(SKIndex!) -> Bool](./api-1450667-skindexflush.md)
  Invokes all pending updates associated with an index and commits them to backing store.
- [func SKIndexCompact(SKIndex!) -> Bool](./api-1443628-skindexcompact.md)
  Invokes all pending updates associated with an index, compacts the index if compaction is needed, and commits all changes to backing store.
- [func SKIndexGetDocumentCount(SKIndex!) -> CFIndex](./api-1449093-skindexgetdocumentcount.md)
  Gets the total number of documents represented in an index.
- [func SKIndexGetMaximumDocumentID(SKIndex!) -> SKDocumentID](./api-1444628-skindexgetmaximumdocumentid.md)
  Gets the highest-numbered document ID in an index.
- [func SKIndexGetMaximumTermID(SKIndex!) -> CFIndex](./api-1444278-skindexgetmaximumtermid.md)
  Gets the highest-numbered term ID in an index.
- [func SKIndexDocumentIteratorCreate(SKIndex!, SKDocument!) -> Unmanaged<SKIndexDocumentIterator>!](./api-1446189-skindexdocumentiteratorcreate.md)
  Creates an index-based iterator for document URL objects (of type [`SKDocument`](./skdocument.md)) owned by a parent document URL object.
- [func SKIndexDocumentIteratorCopyNext(SKIndexDocumentIterator!) -> Unmanaged<SKDocument>!](./api-1442212-skindexdocumentiteratorcopynext.md)
  Obtains the next document URL object (of type [`SKDocument`](./skdocument.md)) from an index using a document iterator.
- [func SKIndexDocumentIteratorGetTypeID() -> CFTypeID](./api-1443022-skindexdocumentiteratorgettypeid.md)
  Gets the type identifier for Search Kit document iterators.
- [func SKIndexGetAnalysisProperties(SKIndex!) -> Unmanaged<CFDictionary>!](./api-1443461-skindexgetanalysisproperties.md)
  Gets the text analysis properties of an index.
- [func SKIndexMoveDocument(SKIndex!, SKDocument!, SKDocument!) -> Bool](./api-1449899-skindexmovedocument.md)
  Changes the parent of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexRemoveDocument(SKIndex!, SKDocument!) -> Bool](./api-1444375-skindexremovedocument.md)
  Removes a document URL object (of type [`SKDocument`](./skdocument.md)) and its children, if any, from an index.
- [func SKIndexRenameDocument(SKIndex!, SKDocument!, CFString!) -> Bool](./api-1448935-skindexrenamedocument.md)
  Changes the name of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexSetMaximumBytesBeforeFlush(SKIndex!, CFIndex)](./api-1448696-skindexsetmaximumbytesbeforeflus.md)
  Not recommended. Sets the memory size limit for updates to an index, measured in bytes. 
- [func SKIndexGetMaximumBytesBeforeFlush(SKIndex!) -> CFIndex](./api-1445329-skindexgetmaximumbytesbeforeflus.md)
  Not recommended. Gets the memory size limit for updates to an index, measured in bytes.
### Working With Text Importers
- [func SKLoadDefaultExtractorPlugIns()](./api-1447859-skloaddefaultextractorplugins.md)
  Tells Search Kit to use the Spotlight metadata importers.
### Working with Documents and Terms
- [func SKDocumentCreateWithURL(CFURL!) -> Unmanaged<SKDocument>!](./api-1442564-skdocumentcreatewithurl.md)
  Creates a document URL object (of type [`SKDocument`](./skdocument.md)) from a [`CFURL`](../CoreFoundation/cfurl.md) object.
- [func SKDocumentCreate(CFString!, SKDocument!, CFString!) -> Unmanaged<SKDocument>!](./api-1443212-skdocumentcreate.md)
  Creates a document URL object (of type [`SKDocument`](./skdocument.md)) based on a scheme, parent, and name.
- [func SKDocumentCopyURL(SKDocument!) -> Unmanaged<CFURL>!](./api-1449624-skdocumentcopyurl.md)
  Builds a [`CFURL`](../CoreFoundation/cfurl.md) object from a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetName(SKDocument!) -> Unmanaged<CFString>!](./api-1442657-skdocumentgetname.md)
  Gets the name of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetParent(SKDocument!) -> Unmanaged<SKDocument>!](./api-1444449-skdocumentgetparent.md)
  Gets the parent of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetSchemeName(SKDocument!) -> Unmanaged<CFString>!](./api-1448262-skdocumentgetschemename.md)
  Gets the scheme name for a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKDocumentGetTypeID() -> CFTypeID](./api-1448891-skdocumentgettypeid.md)
  Gets the type identifier for Search Kit document URL objects.
- [func SKIndexCopyDocumentForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<SKDocument>!](./api-1442760-skindexcopydocumentfordocumentid.md)
  Obtains a document URL object (of type [`SKDocument`](./skdocument.md)) from an index.
- [func SKIndexCopyInfoForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<CFString>?>!, UnsafeMutablePointer<SKDocumentID>!)](./api-1445499-skindexcopyinfofordocumentids.md)
  Gets document names and parent IDs based on document IDs.
- [func SKIndexCopyDocumentRefsForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<SKDocument>?>!)](./api-1445305-skindexcopydocumentrefsfordocume.md)
  Gets document URL objects (of type [`SKDocument`](./skdocument.md)) based on document IDs.
- [func SKIndexCopyDocumentURLsForDocumentIDs(SKIndex!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Unmanaged<CFURL>?>!)](./api-1443501-skindexcopydocumenturlsfordocume.md)
  Gets document URLs based on document IDs.
- [func SKIndexCopyDocumentIDArrayForTermID(SKIndex!, CFIndex) -> Unmanaged<CFArray>!](./api-1448003-skindexcopydocumentidarrayforter.md)
  Obtains document IDs for documents that contain a given term.
- [func SKIndexCopyTermIDArrayForDocumentID(SKIndex!, SKDocumentID) -> Unmanaged<CFArray>!](./api-1446868-skindexcopytermidarrayfordocumen.md)
  Obtains the IDs for the terms of an indexed document.
- [func SKIndexCopyTermStringForTermID(SKIndex!, CFIndex) -> Unmanaged<CFString>!](./api-1442802-skindexcopytermstringfortermid.md)
  Obtains a term, specified by ID, from an index.
- [func SKIndexGetTermIDForTermString(SKIndex!, CFString!) -> CFIndex](./api-1448558-skindexgettermidfortermstring.md)
  Gets the ID for a term in an index.
- [func SKIndexSetDocumentProperties(SKIndex!, SKDocument!, CFDictionary!)](./api-1444576-skindexsetdocumentproperties.md)
  Sets the application-defined properties of a document URL object (of type [`SKDocument`](./skdocument.md)).
- [func SKIndexCopyDocumentProperties(SKIndex!, SKDocument!) -> Unmanaged<CFDictionary>!](./api-1449500-skindexcopydocumentproperties.md)
  Obtains the application-defined properties of an indexed document.
- [func SKIndexGetDocumentState(SKIndex!, SKDocument!) -> SKDocumentIndexState](./api-1443396-skindexgetdocumentstate.md)
  Gets the current indexing state of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
- [func SKIndexGetDocumentTermCount(SKIndex!, SKDocumentID) -> CFIndex](./api-1448341-skindexgetdocumenttermcount.md)
  Gets the number of terms for a document in an index.
- [func SKIndexGetDocumentTermFrequency(SKIndex!, SKDocumentID, CFIndex) -> CFIndex](./api-1447537-skindexgetdocumenttermfrequency.md)
  Gets the number of occurrences of a term in a document.
- [func SKIndexGetTermDocumentCount(SKIndex!, CFIndex) -> CFIndex](./api-1444015-skindexgettermdocumentcount.md)
  Gets the number of documents containing a given term represented in an index.
- [func SKIndexGetDocumentID(SKIndex!, SKDocument!) -> SKDocumentID](./api-1444437-skindexgetdocumentid.md)
  Gets the ID of a document URL object (of type [`SKDocument`](./skdocument.md)) in an index.
### Fast Asynchronous Searching
- [func SKSearchCreate(SKIndex!, CFString!, SKSearchOptions) -> Unmanaged<SKSearch>!](./api-1443079-sksearchcreate.md)
  Creates an asynchronous search object for querying an index, and initiates search.
- [func SKSearchFindMatches(SKSearch!, CFIndex, UnsafeMutablePointer<SKDocumentID>!, UnsafeMutablePointer<Float>!, CFTimeInterval, UnsafeMutablePointer<CFIndex>!) -> Bool](./api-1448608-sksearchfindmatches.md)
  Extracts search result information from a search object.
- [func SKSearchCancel(SKSearch!)](./api-1442083-sksearchcancel.md)
  Cancels an asynchronous search request.
- [func SKSearchGetTypeID() -> CFTypeID](./api-1448621-sksearchgettypeid.md)
  Gets the type identifier for Search Kit search objects.
### Working With Summarization
- [func SKSummaryCreateWithString(CFString!) -> Unmanaged<SKSummary>!](./api-1446229-sksummarycreatewithstring.md)
  Creates a summary object based on a text string.
- [func SKSummaryGetSentenceSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](./api-1444767-sksummarygetsentencesummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom sentence-based summary string.
- [func SKSummaryGetParagraphSummaryInfo(SKSummary!, CFIndex, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!) -> CFIndex](./api-1447517-sksummarygetparagraphsummaryinfo.md)
  Gets detailed information about a body of text for constructing a custom paragraph-based summary string.
- [func SKSummaryGetSentenceCount(SKSummary!) -> CFIndex](./api-1450009-sksummarygetsentencecount.md)
  Gets the number of sentences in a summarization object.
- [func SKSummaryGetParagraphCount(SKSummary!) -> CFIndex](./api-1449304-sksummarygetparagraphcount.md)
  Gets the number of paragraphs in a summarization object.
- [func SKSummaryCopySentenceAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1450287-sksummarycopysentenceatindex.md)
  Gets a specified sentence from the text in a summarization object.
- [func SKSummaryCopyParagraphAtIndex(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1445711-sksummarycopyparagraphatindex.md)
  Gets a specified paragraph from the text in a summarization object.
- [func SKSummaryCopySentenceSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1449700-sksummarycopysentencesummarystri.md)
  Gets a text string consisting of a summary with, at most, the requested number of sentences.
- [func SKSummaryCopyParagraphSummaryString(SKSummary!, CFIndex) -> Unmanaged<CFString>!](./api-1449746-sksummarycopyparagraphsummarystr.md)
  Gets a text string consisting of a summary with, at most, the requested number of paragraphs.
- [func SKSummaryGetTypeID() -> CFTypeID](./api-1444796-sksummarygettypeid.md)
  Gets the type identifier for Search Kit summarization objects.
### Callbacks
- [typealias SKSearchResultsFilterCallBack](./sksearchresultsfiltercallback.md)
  Deprecated. Use `SKSearchCreate` and `SKSearchFindMatches` instead, which do not use a callback.
### Data Types
- [typealias SKDocument](./skdocument.md)
  Defines an opaque data type representing a document’s URL.
- [class SKIndexDocumentIterator](./skindexdocumentiterator.md)
  Defines an opaque data type representing an index-based document iterator.
- [class SKIndex](./skindex.md)
  Defines an opaque data type representing an index.
- [class SKSearch](./sksearch.md)
  Defines an opaque data type representing an asynchronous search.
- [class SKSummary](./sksummary.md)
  Defines an opaque data type representing summarization information.
- [typealias SKDocumentID](./skdocumentid.md)
  Defines an opaque data type representing a lightweight document identifier.
- [class SKSearchResults](./sksearchresults.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [class SKSearchGroup](./sksearchgroup.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [SKDocumentRef](./skdocumentref.md)
  Defines an opaque data type representing a document’s URL.
- [SKIndexDocumentIteratorRef](./skindexdocumentiteratorref.md)
  Defines an opaque data type representing an index-based document iterator.
- [SKIndexRef](./skindexref.md)
  Defines an opaque data type representing an index.
- [SKSearchRef](./sksearchref.md)
  Defines an opaque data type representing an asynchronous search.
- [SKSummaryRef](./sksummaryref.md)
  Defines an opaque data type representing summarization information.
- [SKSearchResultsRef](./sksearchresultsref.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [SKSearchGroupRef](./sksearchgroupref.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
### Constants
- [Text Analysis Keys](./search_kit/text_analysis_keys.md)
  Each of these constants is an optional key in a Search Kit index’s text analysis properties dictionary. The constant descriptions describe the corresponding values for each of these keys. These keys are declared in the `Analysis.h` header file.
- [struct SKDocumentIndexState](./skdocumentindexstate.md)
  The indexing state of a document.
- [typealias SKSearchOptions](./sksearchoptions.md)
  Specifies the search options available for the [`SKSearchCreate(_:_:_:)`](./api-1443079-sksearchcreate.md) function.
- [struct SKIndexType](./skindextype.md)
  Specifies the category of an index.
- [struct SKSearchType](./sksearchtype.md)
  Search Kit ignores the constants in this group. Use asynchronous searching with `SKSearchCreate` instead, which uses query syntax to determine search type.
- [var kSKDocumentStateAddPending: SKDocumentIndexState](./kskdocumentstateaddpending.md)
  Specifies that the document is not in the index but will be added after the index is flushed or closed.
- [var kSKDocumentStateDeletePending: SKDocumentIndexState](./kskdocumentstatedeletepending.md)
  Specifies that the document is in the index but will be deleted after the index is flushed or closed.
- [var kSKDocumentStateIndexed: SKDocumentIndexState](./kskdocumentstateindexed.md)
  Specifies that the document is indexed.
- [var kSKDocumentStateNotIndexed: SKDocumentIndexState](./kskdocumentstatenotindexed.md)
  Specifies that the document is not indexed.
- [var kSKIndexInverted: SKIndexType](./kskindexinverted.md)
  Specifies an inverted index, mapping terms to documents.
- [var kSKIndexInvertedVector: SKIndexType](./kskindexinvertedvector.md)
  Specifies an index type with all the capabilities of an inverted and a vector index.
- [var kSKIndexUnknown: SKIndexType](./kskindexunknown.md)
  Specifies an unknown index type.
- [var kSKIndexVector: SKIndexType](./kskindexvector.md)
  Specifies a vector index, mapping documents to terms.
- [var kSKSearchBooleanRanked: SKSearchType](./ksksearchbooleanranked.md)
  Deprecated. Specifies a query that can include Boolean operators including `'|'`, `'&'`, `'!'`, `'('`, and `')'`.
- [var kSKSearchPrefixRanked: SKSearchType](./ksksearchprefixranked.md)
  Deprecated. Specifies a prefix-based search, which matches terms that begin with the query string.
- [var kSKSearchRanked: SKSearchType](./ksksearchranked.md)
  Deprecated. Specifies a basic ranked search.
- [var kSKSearchRequiredRanked: SKSearchType](./ksksearchrequiredranked.md)
  Deprecated. Specifies a query that can include required (`'+'`) or excluded (`'-'`) terms.
- [Deprecated Text Analysis Keys](./search_kit/deprecated_text_analysis_keys.md)
  Search Kit ignores the `kSKLanguageTypes` constant. It determines language directly by document content.
- [kSKDocumentStateAddPending](./skdocumentindexstate/kskdocumentstateaddpending.md)
  Specifies that the document is not in the index but will be added after the index is flushed or closed.
- [kSKDocumentStateDeletePending](./skdocumentindexstate/kskdocumentstatedeletepending.md)
  Specifies that the document is in the index but will be deleted after the index is flushed or closed.
- [kSKDocumentStateIndexed](./skdocumentindexstate/kskdocumentstateindexed.md)
  Specifies that the document is indexed.
- [kSKDocumentStateNotIndexed](./skdocumentindexstate/kskdocumentstatenotindexed.md)
  Specifies that the document is not indexed.
- [kSKIndexInverted](./skindextype/kskindexinverted.md)
  Specifies an inverted index, mapping terms to documents.
- [kSKIndexInvertedVector](./skindextype/kskindexinvertedvector.md)
  Specifies an index type with all the capabilities of an inverted and a vector index.
- [kSKIndexUnknown](./skindextype/kskindexunknown.md)
  Specifies an unknown index type.
- [kSKIndexVector](./skindextype/kskindexvector.md)
  Specifies a vector index, mapping documents to terms.
- [kSKSearchBooleanRanked](./sksearchtype/ksksearchbooleanranked.md)
  Deprecated. Specifies a query that can include Boolean operators including `'|'`, `'&'`, `'!'`, `'('`, and `')'`.
- [kSKSearchPrefixRanked](./sksearchtype/ksksearchprefixranked.md)
  Deprecated. Specifies a prefix-based search, which matches terms that begin with the query string.
- [kSKSearchRanked](./sksearchtype/ksksearchranked.md)
  Deprecated. Specifies a basic ranked search.
- [kSKSearchRequiredRanked](./sksearchtype/ksksearchrequiredranked.md)
  Deprecated. Specifies a query that can include required (`'+'`) or excluded (`'-'`) terms.
### Legacy Support for Synchronous Searching
- [SKSearchGroupCreate](./api-1448627-sksearchgroupcreate.md)
  Creates a search group as an array of references to indexes.
- [SKSearchGroupCopyIndexes](./api-1448615-sksearchgroupcopyindexes.md)
  Obtains the indexes for a search group.
- [SKSearchGroupGetTypeID](./api-1448637-sksearchgroupgettypeid.md)
  Deprecated. Use asynchronous searching with SKSearchCreate instead, which does not employ search groups.
- [SKSearchResultsCreateWithDocuments](./api-1448629-sksearchresultscreatewithdocumen.md)
  Finds documents similar to given example documents.
- [SKSearchResultsGetInfoInRange](./api-1448618-sksearchresultsgetinfoinrange.md)
  Extracts information from a Search Kit query result.
- [SKSearchResultsCopyMatchingTerms](./api-1448612-sksearchresultscopymatchingterms.md)
  Obtains the terms in a document that match a query.
- [SKSearchResultsGetCount](./api-1448598-sksearchresultsgetcount.md)
  Gets the total number of found items in a search.
- [SKSearchResultsGetTypeID](./api-1448603-sksearchresultsgettypeid.md)
  Gets the type identifier for Search Kit search results.
- [SKSearchResultsCreateWithQuery](./api-1448610-sksearchresultscreatewithquery.md)
  Queries the indexes in a search group.

## See Also

### Related Documentation
- [Search Kit Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SearchKitConcepts/searchKit_intro/searchKit_intro.html#//apple_ref/doc/uid/TP40001071)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/search_kit)*
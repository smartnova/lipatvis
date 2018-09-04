# About this reposiotry

In 2016, Federico and others have published an impressive survey paper (Federico+ 2016)

> Federico, P., Heimerl, F., Koch, S., and Miksch, S., [/ [A Survey on Visual Approaches for Analysing Scientific Literature and Patents http://dx.doi.org/10.1109/TVCG.2016.2610422] ], IEEE Transactions on Visualisation and Computer Graphics, 2016.

They also provided [a visual interface](http://ieg.ifs.tuwien.ac.at/%7Efederico/LiPatVis/) to the technical contributions mentioned in their survey using the [SurVis system](https://github.com/fabian-beck/survis).  The SurVis system maintains bibliographic database stored in BibTeX format.  The BibTeX of the above mentioned survey paper can be downleded by clicking on the **download BibTeX** button found in the bottom-left corner of the SurVis view.

## Then why am I distributing my own version of BibTeX?

![The BibTeX file loaded on BibDesk app](https://gyazo.com/c4b7b796abcebc0090428046ac73d81f.png)

The BibTeX distributed via SurVis is great.  It contains all the technical papers mentioned in the paper.  The contents of **Keywords** is based on the taxonomy presented in the paper.  I greatly appreciate the survey authors for sharing bibliographic list and taxonomy in a machine readable form.

That said, I wanted to add and modify a bit more information to the BibTeX database.

1. The survey paper employs numeric citation form (like, `[12]`) and does not provide hyperlinks.  It is bothering to identify which paper is mentioned in the paragraph.  My version of BibTeX containes the `Citeno` field, which annotetes the citation number used in the survey paper to each BibTeX entry.

    My version of BibTeX is optimized for BibDesk, a popular BibTeX management app for Mac.  By sorting the entries according to `Citeno`, you can easily identify the paper refenced in the paper.  If you want to find a peper by citation number, you can use BibDesk's Search box.

1. I have added the section information in the `Keywords` field of the entry.  Simply clicking on the section title that you see in the Caterories section of the sidebar, you immediately show the list of papers mentioned in the section.

    In converse, if you select a peper, you can find which sections for the survey that paper appears.  For example, if you select (Gorg 2013), you see this paper appears in Sections 3.1.2, 3.1.3, 3.4.2, and 3.5.5.

1. I also added the `N_Secs` field that represents the number of sections that the entry appears in the survey.  For example, the `N_Secs` field for (Gorg 2013) is 4.  If you sort the entries according to `N_Secs` field, you can see the list of papers that the survey authors considers are important.



# What is `references.pdf`?

My version of BibTeX database is optimized for BibDesk app for Mac.  As I am not a Windows user, I can not name a compatible software on Windows platform.  For the convenience of Windows users, I provided a PDF file named (`references.pdf`).

# Viewing the BibTeX file using BibDesk

BibDesk is a powerfull browser for BibTeX databases.  It is contained in MacTeX and can be found under `/Applications/TeX`.

It is possible to view the BibDesk file but to enjoy the full annotations, please apply the following settings:

- Add custom fields `Categories` to the group fields by using BibDesk menu: **View / Group Fields / Add Group Field...**

    This setting adds section list and taxonomy list to the side bar.

- Right-click on one of the title of the entry list (the main pane of BibDesk) and choose **Add other ...** and add `Citeno` and `N_Secs`.  This settings add the fields as new columns to the right of the column titles.  You may want to move them at the left most position of the table by dragging them to the left.



# Hints on making use of the BibTeX

- Select a section from the **Categories** from the side bar.  You will see the list of papers mentioned in the section.

    Selecting **3.2.3 Citation - Patterns** will show papers [57, 67, 68, ..., 74].

- Select an entry form the list of the papers and look at the **Categories** in the sidebar.  Sections that this paper is mentioned and paper categories of the paper is highlighted.  Selection of multiple papers highlights such informaiton collectively.

    For example, if I choose (Koch 2011, [23]), I easily find the following facts:
    
    - The paper is mentioned in Sections 3.1.1 (Text - Entity) and 3.5.4 (Sequential approaches and multiple views).
    - It deals with patent visualization (datatype/pattets).
    - Its targets of analysis are citation, meta information (data/{citations, meta, text})
    - It supports three kinds of tasks (task/{1-entities, 3-patterns, 4-temporal)

- Select a category entry from the **Categories** in the sidebar.  You find a list of papers that contributes to this category

    For example, if I select **multiple/5-views** category, I find related papers [0, 30, 34, 39, 55, ...].

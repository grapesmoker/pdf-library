# pdf-library

pdf-library is a program for keeping track of your PDFs. It allows you to build a databse complete with metadata about the file. It's particularly useful for keeping track of things like scientific papers.

# Running it

Clone the repo, go to the directory you cloned to, and run `./main`.

# Requirements

You'll need to install Qt5 and the Python bindings to Qt5, as well as ImageMagick (used for previews). You need to have `sqlalchemy`, `Wand` (an interface to ImageMagick), and `PyPDF2` installed; you can get these by doing `pip install -r requirements.txt`. There may be others that I'm forgetting though.

# Features

Right now, you can create a new library and populate it with all the PDF files that live under the library root (this can take a while if you have a lot of files). Once you do that, you'll be able to see all the files and authors by clicking on the appropriate selection on the left pane. Most of the capability right now is oriented towards working with the documents themselves: you can assign authors to documents, change their title, and rename them on the file system.

# Future work

More metadata capabilities will be added in the future. In addition, I plan to add search, possibly powered by Apache Tika. If you're really lucky, I'll make the interface less ugly.

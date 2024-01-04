    function get_pdf_file(path){
        // Specify the path to your PDF file
        const pdfFile = path;

        // Specify the container for the PDF viewer
        const container = document.getElementById('pdf-viewer');

        // Initialize PDF.js
        pdfjsLib.getDocument(pdfFile).promise.then(pdfDoc => {
          // Loop through each page and render it in the viewer
          for (let pageNum = 1; pageNum <= pdfDoc.numPages; pageNum++) {
            pdfDoc.getPage(pageNum).then(page => {
              const canvas = document.createElement('canvas');
              container.appendChild(canvas);

              const context = canvas.getContext('2d');
              const viewport = page.getViewport({ scale: 1.5 });

              canvas.height = viewport.height;
              canvas.width = viewport.width;

              const renderContext = {
                canvasContext: context,
                viewport: viewport
              };

              page.render(renderContext);
            });
          }
        });
    }

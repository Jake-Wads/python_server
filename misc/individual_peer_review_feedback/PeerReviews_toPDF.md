# Steps to Convert Google Sheet to Individual PDFs

### 1. Go to Individual Project - Peer Review Google Form
- Open <a href = "https://www.classroom.google.com">classroom.google.com</a>
- Select appropriate class
- Go to Classwork Tab
- Choose Individual Project topic
- Scroll down to Individual Project - Peer Review classwork exercise 
- Click on attached Google Form
![step1](https://i.pinimg.com/originals/14/a6/bb/14a6bb42a084fc72cab7ca432b752ead.png)

### 2. Open the responses in Google Sheets
- Select Edit icon at the bottom right of the form
- Click View in Sheets button at the top of right of Responses page
![step2](https://i.pinimg.com/originals/12/79/f9/1279f9b37efb5435c309fe8efe1e834f.png)

### 3. Open Apps Script
- Extensions > Apps Script

![step3](https://i.pinimg.com/originals/92/88/31/928831c9e41e362b61f5e97053e01ee5.png)

### 4. Create a new Script File
![step4](https://i.pinimg.com/originals/c7/49/30/c74930cdbfad98b0d60f034dff784040.png)

### 5. Rename `rowtotabs`

![step5](https://i.pinimg.com/originals/18/af/e1/18afe1e7c2a01136264ba4d86e1c6690.png)

### 6. Paste in the following code and `Cmd + S`
>```
>function exportRowsToNewTabs() {
>  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
>  var data = sheet.getDataRange().getValues();
>  var nameCounter = {}; // Object to track tab name occurrences
>  
>  for (var i = 1; i < data.length; i++) {
>    var newRow = data[i];
>    var newSheetName = newRow[2]; // Assumes the third cell of the exported row is used for the tab name
>    
>    // Check if the tab name already exists, and append a counter if needed
>    if (nameCounter[newSheetName]) {
>      nameCounter[newSheetName]++;
>      newSheetName = newSheetName + " (" + nameCounter[newSheetName] + ")";
>    } else {
>      nameCounter[newSheetName] = 1;
>    }
>    
>    // Create a new sheet
>    var newSheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet(newSheetName);
>    
>    // Set values in the new sheet (transposed)
>    for (var j = 0; j < newRow.length; j++) {
>      newSheet.getRange(j + 1,1).setValue(data[0][j]);
>      newSheet.getRange(j + 1,2).setValue(newRow[j]);
>      }
>  }
>}
>
>```

### 7. Repeat Steps 4-6 for:

- format.gs
>```
>function formatAllTabs() {
>  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
>  var sheets = spreadsheet.getSheets();
>  
>  for (var i = 1; i < sheets.length; i++) {
>    var sheet = sheets[i];
>    
>    // Set word wrap for all cells
>    var range = sheet.getDataRange();
>    range.setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
>    
>    // Set larger cell width for all columns
>    var columns = range.getNumColumns();
>    for (var j = 1; j <= columns; j++) {
>      sheet.setColumnWidth(j, 540);
>    }
>  }
>}
>
>```

- alphatabs.gs
>```
>function sortSheetsAsc() {
>  var ss = SpreadsheetApp.getActiveSpreadsheet();
>  var sheets = ss.getSheets();
>  var sheetNameArray = [];
>
>  for (var i = 0; i < sheets.length; i++) {
>    sheetNameArray.push(sheets[i].getName());
>  }
>
>  sheetNameArray.sort();
>
>  for( var j = 0; j < sheets.length; j++ ) {
>    ss.setActiveSheet(ss.getSheetByName(sheetNameArray[j]));
>    ss.moveActiveSheet(j + 1);
>  }
>}
>
>function sortSheetsDesc() {
>  var ss = SpreadsheetApp.getActiveSpreadsheet();
>  var sheets = ss.getSheets();
>  var sheetNameArray = [];
>
>  for (var i = 0; i < sheets.length; i++) {
>    sheetNameArray.push(sheets[i].getName());
>  }
>
>  sheetNameArray.sort().reverse();
>
>  for( var j = 0; j < sheets.length; j++ ) {
>    ss.setActiveSheet(ss.getSheetByName(sheetNameArray[j]));
>    ss.moveActiveSheet(j + 1);
>  }
>}
>
>function sortSheetsRandom() {
>  var ss = SpreadsheetApp.getActiveSpreadsheet();
>  var sheets = ss.getSheets();
>  var sheetNameArray = [];
>
>  for (var i = 0; i < sheets.length; i++) {
>    sheetNameArray.push(sheets[i].getName());
>  }
>
>  sheetNameArray.sort().sort(() => (Math.random() > .5) ? 1 : -1);;
>
>  for( var j = 0; j < sheets.length; j++ ) {
>    ss.setActiveSheet(ss.getSheetByName(sheetNameArray[j]));
>    ss.moveActiveSheet(j);
>  }
>}
>
>function onOpen() {
>  var spreadsheet = SpreadsheetApp.getActive();
>  var menuItems = [
>    {name: 'Sort Sheets A ➜ Z', functionName: 'sortSheetsAsc'},
>    {name: 'Sort Sheets Z ➜ A', functionName: 'sortSheetsDesc'},
>    {name: 'Randomize Sheet Order 🎲', functionName: 'sortSheetsRandom'}
>  ];
>  spreadsheet.addMenu('Sheet Tools', menuItems);
>}
>```

### 8. Once all Scripts have been created and **saved**, select the script one at a time and run in the following order: 
1. `rowtotabs.gs`
2. `format.gs`
3. `alphatabs.gs`
![step8](https://i.pinimg.com/originals/72/3a/fc/723afcc1b3b5c5f6ad14581aca526093.png)

### 9. Go back to the Google sheet and Hide the original master tab
![step9](https://i.pinimg.com/originals/97/93/ed/9793ed14962451ad5bd6e11cbb76d78b.png)

### 10. Export as a pdf (I changed my formatting to Legal sized and portrait for aesthetic purposes)
![step10](https://i.pinimg.com/originals/88/43/5c/88435c5df19cebf902d05a47e6e73cbe.png)
![step10.1](https://i.pinimg.com/originals/74/e7/13/74e7139f6c0acdedb2167b25ba4c3fa2.png)

### 11. Move PDF file out of Downloads to a new location


### 12. I personally used an ipynb to run the function on all of my students: reference the ex in DocStrings

```
import PyPDF2

def split_pdf(input_file, output_file, start_page, end_page):
    """
    # Example usage
    input_file = 'input.pdf'
    output_file = 'output.pdf'
    start_page = 2  # Starting page (0-based index)
    end_page = 4    # Ending page (0-based index)
    
    *******Check your pdf file, incase a student has more than 2 reviewers
    example: split_pdf('Peer_Review-Responses.pdf', 'Alexia.pdf', 0,1)
    """

    with open(input_file, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        
        if start_page < 0 or start_page >= len(pdf.pages) or end_page < start_page or end_page >= len(pdf.pages):
            print('Invalid page range.')
            return
        
        writer = PyPDF2.PdfWriter()
        
        for page_num in range(start_page, end_page + 1):
            page = pdf.pages[page_num]
            writer.add_page(page)
        
        with open(output_file, 'wb') as output:
            writer.write(output)
        
        print('PDF split successful.')
```

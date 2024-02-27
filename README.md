## Flask Application Design
### HTML Files
- `index.html`:
  - Purpose: Serves as the application's main page.
  - Content: Displays a concise explanation of the app's functionality and a primary navigation bar.
- `news.html`:
  - Purpose: Houses the news summary content.
  - Content: Includes a dynamic section to display the generated news summaries based on user selection.
- `summarize_news.html`:
  - Purpose: Presents a frontend for news summary generation.
  - Content: Contains a form where users can select a news category (financial, sports, politics) and submit it for summary.

### Routes
- `/`:
 - Purpose: Redirects the user to the news summary page.
- `/summarize_news`:
  - Purpose: Handles the user's request to generate a news summary.
  - Method: POST
  - Request Body: Category of news selected by the user.
  - Response: Renders the `news.html` page with the generated summary.
- `/news`:
  - Purpose: Displays the news summary based on the selected category.
  - Method: GET
  - Parameters:
    - Category: Financial (Tuesday), Politics (Friday), Sports (UFC and F1) (Monday).
  - Response: Renders the `news.html` page with the relevant category's summary.
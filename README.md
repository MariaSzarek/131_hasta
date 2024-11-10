# Hasta reservation

This is an application that allows users to view available time slots for courts. 
Free slots must be longer than 1 hour.


#### Example return:
   ```bash
Dzisiejszy dzień miesiąca to: 9
Dzień 31 nie istnieje na stronie.   
W dniu 12 od godziny 12:30 do 14:00 kort 10 jest wolny.
W dniu 12 od godziny 12:00 do 13:30 kort 9 jest wolny.
W dniu 13 od godziny 10:30 do 13:30 kort 9 jest wolny.
W dniu 14 od godziny 10:30 do 12:00 kort 7 jest wolny.
   ```


## Running Locally

To run this application locally, follow these steps:

#### Prerequisites

- Python 3.x installed on your machine
- Pip package manager installed
- Virtualenv installed

#### Setting up Virtual Environment

1. Clone this repository to your local machine:

   ```bash
   git clone -b branch_name <repository address>
   ```

2. Navigate to the project directory:

   ```bash
   cd 131_hasta
   ```

3. Create a virtual environment:

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment (on Windows):

   ```bash
   env\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run script:

   ```bash
   python main.py
   ```
   
7. Testing:

   ```bash
   pytest tests/test_courts.py
   ```




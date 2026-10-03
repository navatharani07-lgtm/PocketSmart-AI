from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

LOGIN_PAGE = """
<!DOCTYPE html>
<html><head><title>PocketSmart AI - Login</title>
<style>
body{margin:0;font-family:Arial;background:#eef0ff}
.nav{background:white;padding:12px 20px;color:#6c5cff;font-weight:bold;box-shadow:0 1px 3px #ddd}
.wrap{display:flex;justify-content:center;align-items:center;min-height:85vh}
.box{background:white;width:320px;padding:28px;border-radius:16px;box-shadow:0 8px 25px #0002;text-align:center}
input{width:100%;padding:10px;margin:6px 0 12px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
.btn{width:100%;padding:11px;background:#6c5cff;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;text-decoration:none;display:block;text-align:center}
</style></head><body>
<div class="nav">🧠 PocketSmart AI</div>
<div class="wrap"><div class="box">
<div style='background:#f0eeff;width:45px;height:45px;border-radius:50%;margin:0 auto;line-height:45px;font-size:20px'>👑</div>
<h3 style='margin:12px 0 5px'>Welcome Back!</h3>
<p style='font-size:11px;color:#888;margin:0 0 18px'>Login to continue using your PocketSmart AI assistant.</p>
<div style='text-align:left;font-size:12px'>
📧 Email<br><input value='anishasivara07@gmail.com'><br>
🔒 Password<br><input type='password' value='******'><br>
<a href='/dashboard' class="btn">🔒 Login to PocketSmart</a>
<p style='font-size:11px;text-align:center;margin-top:12px'>Don't have an account? <a href='/register' style='color:#6c5cff'>Create Account</a></p>
</div></div></div>
</body></html>
"""

DASHBOARD_PAGE = """
<!DOCTYPE html>
<html><head><title>PocketSmart AI - Dashboard</title>
<style>
body{margin:0;font-family:Arial;background:#eef0ff}
.nav{background:white;padding:12px 20px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 1px 3px #ddd}
.nav a{text-decoration:none;color:#666;font-size:12px;margin-left:10px}
.nav b{color:#6c5cff}
.center{max-width:900px;margin:0 auto;padding:20px}
.blue{max-width:900px;margin:0 auto;background:#6c5cff;color:white;padding:25px;border-radius:12px}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin:15px 0}
.card{background:white;border-radius:12px;padding:20px;text-align:center;box-shadow:0 2px 8px #0001}
.btn{background:#6c5cff;color:white;padding:8px 16px;border-radius:6px;text-decoration:none;display:inline-block;margin-top:10px;font-size:12px}
.activity{background:white;border-radius:12px;padding:20px;text-align:center;box-shadow:0 2px 8px #0001;margin-top:15px}
.mini{background:#f5f3ff;padding:15px;border-radius:10px}
</style></head><body>
<div class="nav"><b>🧠 PocketSmart AI</b><div><a href='/'>🏠 Home</a><a href='/dashboard'>📊 Dashboard</a><a href='/' style='color:#ff6b6b'>🚪 Logout</a></div></div>
<div class="center">
<div class="blue"><h2 style='margin:0'>👋 Welcome to PocketSmart AI!</h2><p style='font-size:13px;margin:8px 0 0'>Plan your budget smartly and get personalized AI recommendations.</p></div>
<div class="grid">
<div class="card"><div style='font-size:24px'>🏠</div><h4>Home Interior</h4><p style='font-size:11px;color:#666'>Plan your home interior according to your budget and requirements.</p><a class="btn" href='#'>Start Planning</a></div>
<div class="card"><div style='font-size:24px'>🎉</div><h4>Party Planner</h4><p style='font-size:11px;color:#666'>Create a smart party plan based on your budget, guests and event.</p><a class="btn" href='#'>Plan Party</a></div>
<div class="card"><div style='font-size:24px'>💎</div><h4>Jewelry</h4><p style='font-size:11px;color:#666'>Get jewelry recommendations based on your occasion and personal style.</p><a class="btn" href='#'>Find Jewelry</a></div>
</div>
<div class="activity">
<b>📊 Your Activity</b><p style='font-size:11px;color:#888'>Track your PocketSmart AI recommendations.</p>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:15px 0'>
<div class="mini">🏠<br><b style='font-size:12px'>Home<br>0</b><br><span style='font-size:10px;color:#888'>Recommendations</span></div>
<div class="mini">🎉<br><b style='font-size:12px'>Party<br>1</b><br><span style='font-size:10px;color:#888'>Recommendations</span></div>
<div class="mini">💎<br><b style='font-size:12px'>Jewelry<br>1</b><br><span style='font-size:10px;color:#888'>Recommendations</span></div>
</div>
<div style='background:#f5f3ff;padding:12px;border-radius:8px'><span style='font-size:11px'>📦 Total Recommendations</span><br><b style='color:#6c5cff;font-size:18px'>2</b></div>
</div>
<div class="activity"><b style='font-size:13px'>📜 Recommendation History</b><p style='font-size:11px;color:#888'>View your previous AI recommendations and budget plans.</p><a class="btn" href='#'>View History</a></div>
</div></body></html>
"""

@app.get("/", response_class=HTMLResponse)
async def first_page():
    return LOGIN_PAGE  # <-- First page is LOGIN

@app.get("/login", response_class=HTMLResponse)
async def login():
    return LOGIN_PAGE

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return DASHBOARD_PAGE

@app.get("/register", response_class=HTMLResponse)
async def register():
    return LOGIN_PAGE.replace("Welcome Back!", "Create Account").replace("Login to continue", "Create your new account").replace("Login to PocketSmart", "Create Account")
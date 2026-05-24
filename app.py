from flask import Flask, render_template, request
from datetime import datetime, timedelta

projects_list = [

    {
        "name": "Cookie Generator",
        "header_link": "high_academy_project_post",
        "description": "A fun Python project that generates random cookie recipes using PyQt6 and AllRecipes.",
        "language": ["Python"],
        "status": "Completed",
        "github": "https://github.com/TiffanyCM/Cookie-Recipe-Generator",
        "date": "12-28-2025",
        "image": "images/project images/cookie generator images/cookie_generator_image.png"
    },

    {
        "name": "Robin in Space",
        "header_link": "high_academy_project_post",
        "description": "A Python game using the Pygame library. Fly through space, avoid asteroids, and defeat enemy space birds in order to get back home! This is an ongoing passion project of mine.",
        "language": ["Python"],
        "status": "In Progress",
        "github":"https://github.com/TiffanyCM/High-Academy",
        "date": None,
        "image": "images/project images/robin in space images/title_page.png"
    },

    {
        "name": "High Academy",
        "header_link": "high_academy_project_post",
        "description": "High Academy is my senior project at Wilmington University. It is an educational platform featuring interactive trigonometry and algebra lessons and quizzes designed for high school students.",
        "language": ["Python", "HTML/CSS"],
        "status": "Completed",
        "github": "https://github.com/TiffanyCM/High-Academy",
        "date": "05-03-2026",
        "image": "images/project images/high academy images/high_academy_home_image.png"
    }




]


blog_list = [

    
    {
        "name": "C# Inventory Management App Part 1",
        "description": "This week, I plan on starting an inventory management application for a grocery store using C#. This project will demonstrate my current skills as I continue learning GUI design.",
        "date": "05-24-2026",
        "image": "images/blog list images/grocery_store_image.jpeg",
        "link": "csharp_inventory_management_post"
    }

    ,


    {
        "name": "Hello World!",
        "description": "Hello! This is my first blog post, and the start of something cool. I want to keep track of my computer science learning journey. Every week, I plan on uploading a blog post about ideas or small projects I am working on.",
        "date": "05-20-2026",
        "image": "images/blog list images/HelloWorld.png",
        "link": "hello_world_post"
    }



]






app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    return render_template("index.html")


@app.route("/projects")
def projects():

    sort = request.args.get("sort", "Newest First")
    language = request.args.get("language", "All")
    status = request.args.get("status", "All")
    date_filter = request.args.get("date", "All Time")

    filtered_projects = projects_list.copy()



    if language != "All":

        filtered_projects = [
            project for project in filtered_projects
            if language in project["language"]
        ]



    if status != "All":

        filtered_projects = [
            project for project in filtered_projects
            if project["status"] == status
        ]

    today = datetime.today()



    if date_filter == "This Year":

        filtered_projects = [
            project for project in filtered_projects
            if project["date"] is not None
            and datetime.strptime(project["date"], "%m-%d-%Y").year == today.year
        ]

    elif date_filter == "This Month":

        filtered_projects = [
            project for project in filtered_projects
            if project["date"] is not None
            and datetime.strptime(project["date"], "%m-%d-%Y").year == today.year
            and datetime.strptime(project["date"], "%m-%d-%Y").month == today.month
        ]

    elif date_filter == "Last 30 Days":

        thirty_days_ago = today - timedelta(days=30)

        filtered_projects = [
            project for project in filtered_projects
            if project["date"] is not None
            and datetime.strptime(project["date"], "%m-%d-%Y") >= thirty_days_ago
        ]



    if sort == "Newest First":

        filtered_projects.sort(
            key=lambda project:
            datetime.strptime(project["date"], "%m-%d-%Y")
            if project["date"] is not None
            else datetime.min,
            reverse=True
        )

    elif sort == "Oldest First":

        filtered_projects.sort(
            key=lambda project:
            datetime.strptime(project["date"], "%m-%d-%Y")
            if project["date"] is not None
            else datetime.min
        )

    elif sort == "A-Z":

        filtered_projects.sort(
            key=lambda project: project["name"]
        )

    elif sort == "Z-A":

        filtered_projects.sort(
            key=lambda project: project["name"],
            reverse=True
        )

    return render_template("projects.html", projects=filtered_projects)









@app.route("/development_blog")

def development_blog():

    return render_template("development_blog.html", blogs=blog_list)




@app.route("/blog_posts/blog_post_5_24_2026")

def csharp_inventory_management_post():

    return render_template("project_posts/blog_post_5_24_2026.html")




if __name__ == "__main__":

    app.run(debug=True)
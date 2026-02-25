<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assessments - LogBook</title>
    <link rel="icon" type="image/x-icon" href="/static/favicon.svg">

    <script>
        // Prevent flash of white in dark mode - runs before CSS/page render
        if (localStorage.getItem('daynight-theme') === 'carbon') {
            document.documentElement.classList.add('carbon');
        }
    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link rel="stylesheet" href="../static/logbook.css">

</head>
<body>
    <div class="app-container">
        <!-- Top Navigation -->
        <nav class="top-nav">
            <div class="nav-container">
                <div class="nav-left">
                    <a href="/" class="logo">

                        <div class="logo-icon">
                            <svg viewBox="0 0 120 110" xmlns="http://www.w3.org/2000/svg" >
                                <g>
                                    <g>
                                        <path fill="#cc3551" d="M108,24h-7.2r23l4.723,3.75L105.113,32H108c4.41,0,8,3.586,8,8v48c0,4.414-3.59,8-8,8H68v4
                                            c0,2.211-1.789,4-4,4s-4-1.789-4-4v-4H20c-4.41,0-8-3.586-8-8V40c0-4.414,3.59-8,8-8h3.707l0.543-3.25L29,24h-9
                                            c-8.836,0-16,7.164-16,16v48c0,8.836,7.164,16,16,16h32.738c1.656,4.648,6.055,8,11.262,8s9.605-3.352,11.262-8H108
                                            c8.836,0,16-7.164,16-16V40C124,31.164,116.836,24,108,24z"/>
                                    </g>
                                </g>
                                <path fill="#f03271" d="M52,40L52,40H36l0,0v-8l0,0h16l0,0V40z"/>
                                <path fill="#f03271" d="M52,56L52,56H36l0,0v-8l0,0h16l0,0V56z"/>
                                <path fill="#f03271" d="M52,72L52,72H36l0,0v-8l0,0h16l0,0V72z"/>
                                <path fill="#f03271" d="M92,40L92,40H76l0,0v-8l0,0h16l0,0V40z"/>
                                <path fill="#f03271" d="M92,56L92,56H76l0,0v-8l0,0h16l0,0V56z"/>
                                <path fill="#f03271" d="M92,72L92,72H76l0,0v-8l0,0h16l0,0V72z"/>
                                <path fill="#f03271" d="M84,16c-6.914,0-13.785,1.852-20,5.367C57.785,17.852,50.914,16,44,16c-8.422,0-16.844,2.602-24,7.82
                                    c0,16.273,0,64.93,0,65.18c0,2.211,1.789,4,4,4c0.395,0,13.832-4.82,20-4.82c6.355,0,12.656,1.625,18.461,4.609l0.066-0.039
                                    l0.004-0.008c0.457,0.18,0.945,0.297,1.469,0.297s1.012-0.117,1.469-0.297l0.004,0.008l0.066,0.039
                                    C71.344,89.805,77.645,88.18,84,88.18c6.168,0,19.605,4.82,20,4.82c2.211,0,4-1.789,4-4c0-0.25,0-48.906,0-65.18
                                    C100.844,18.602,92.422,16,84,16z M28,82.844V28.195c4.875-2.742,10.336-4.172,16-4.172s11.125,1.43,16,4.172
                                    c0,12.883,0,41.766,0,54.648c-5.098-1.781-10.484-2.688-16-2.688S33.098,81.063,28,82.844z M100,82.844
                                    c-5.098-1.781-10.484-2.688-16-2.688s-10.902,0.906-16,2.688c0-12.883,0-41.766,0-54.648c4.875-2.742,10.336-4.172,16-4.172
                                    s11.125,1.43,16,4.172V82.844z"/>
                            </svg>
                        </div>
                        LogBook
                    </a>
                    <div class="nav-menu">
                        <div class="nav-item">
                            <a href="/" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <rect x="3" y="3" width="7" height="7" rx="1"/>
                                    <rect x="14" y="3" width="7" height="7" rx="1"/>
                                    <rect x="3" y="14" width="7" height="7" rx="1"/>
                                    <rect x="14" y="14" width="7" height="7" rx="1"/>
                                </svg>
                                Dashboard
                            </a>
                        </div>
                        <div class="nav-item">
                            <a href="tasks.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                                </svg>
                                Tasks
                            </a>
                        </div>
                        <div class="nav-item">
                            <a href="assessment.html" class="nav-link active">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                    <polyline points="22,6 12,13 2,6"/>
                                </svg>
                                Assessment
                            </a>
                        </div>
                        <div class="nav-item">
                            <a href="logs.html" class="nav-link">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <line x1="18" y1="20" x2="18" y2="10"/>
                                    <line x1="12" y1="20" x2="12" y2="4"/>
                                    <line x1="6" y1="20" x2="6" y2="14"/>
                                </svg>
                                Logs
                            </a>
                        </div>
                    </div>
                </div>
                <div class="nav-right">
                    <div class="theme-toggle">
                        <button class="theme-btn theme-btn-snow active" onclick="setTheme('snow')" title="Snow Edition">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="5"/>
                                <line x1="12" y1="1" x2="12" y2="3"/>
                                <line x1="12" y1="21" x2="12" y2="23"/>
                                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
                                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
                                <line x1="1" y1="12" x2="3" y2="12"/>
                                <line x1="21" y1="12" x2="23" y2="12"/>
                                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
                                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
                            </svg>
                        </button>
                        <button class="theme-btn theme-btn-carbon" onclick="setTheme('carbon')" title="Carbon Edition">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Page Header -->
            <div class="page-header" style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <h1 class="greeting">Assessments</h1>
                    <p class="greeting-sub">What I have to do to successfully graduate this year.</p>
                </div>
            </div>

            <!-- Currently important assessments or some statistics here regarding assessments -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-label">Podatkovne baze 1</div>
                    <div class="stat-value">Project</div>
                    <div class="stat-change positive"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>+18.2% vs last period</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Counter</div>
                    <div class="stat-value">5 exams to finish line!</div>
                    <div class="stat-change positive"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>+12.5% vs last period</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Gotta study this week:</div>
                    <div class="stat-value">Računalništvo 1: Vaje</div>
                    <div class="stat-change positive"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>+8.7% vs last period</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Don't forget about</div>
                    <div class="stat-value">Homework! All subjects</div>
                    <div class="stat-change negative"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/></svg>+2.1% vs last period</div>
                </div>
            </div>

            <!-- Assessments Table -->
            <div class="card">
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>id</th>
                                <th>Subject</th>
                                <th>Type</th>
                                <th>Assessment</th>
                                <th>Created on</th>
                                <th>Due date</th>
                                <th>Done on</th>
                                <th>Grade</th>
                            </tr>
                        </thead>
                        <tbody id = "table-body">
                        <!-- Script to insert data -->
                            <script>
                                const assessments = {{!assessments}};
                                $(document).ready(function () {
                                    console.log("assessments: " + assessments.toString());
                                    for (const a of assessments) {
                                        console.log("item:", a);
                                        console.log("assessment field:", a.id);
                                        $("#table-body").append(`
                                        <tr>
                                            <td>${a.id}</td>
                                            <td>${a.subject_name}</td>
                                            <td>${a.type}</td>
                                            <td>${a.title}</td>
                                            <td>${a.createdOn == "NULL" || a.createdOn == "None" ? "" : a.createdOn}</td>
                                            <td>${a.dueDate}</td>
                                            <td>${a.doneOn == "NULL" || a.doneOn == "None" ? "Not done yet" : a.doneOn}</td>
                                            <td>${a.grade == "NULL" || a.grade == "None" ? "Not yet graded" : a.grade}</td>
                                        </tr>
                                        `);
                                    }
                                });
                            </script>

                        </tbody>
                    </table>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <p>&copy; 2026 LogBook. Created by <a href="" target="_blank" rel="nofollow">Tea Kneževič</a></p>
        </footer>
    </div>

    <script src="../static/logbook.js"></script>
</body>
</html>
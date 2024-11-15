"use client";

import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import {
  Rocket,
  Satellite,
  Users,
  Globe,
  AlertTriangle,
  Moon,
  Sun,
} from "lucide-react";
import { setToken } from "@/actions/setToken";

export default function SpaceDashboard() {
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    const setTokenAsync = async () => {
      await setToken();
    };
    setTokenAsync();
  }, []);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [darkMode]);

  return (
    <div className={`min-h-screen p-4 space-y-4 bg-background text-foreground`}>
      <header className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Space Exploration Dashboard</h1>
        <div className="flex items-center gap-4">
          <Button
            variant="outline"
            size="icon"
            onClick={() => setDarkMode(!darkMode)}
          >
            {darkMode ? (
              <Sun className="h-[1.2rem] w-[1.2rem]" />
            ) : (
              <Moon className="h-[1.2rem] w-[1.2rem]" />
            )}
          </Button>
          <Button onClick={() => window.location.href = "/user"}>Create User</Button>
        </div>
      </header>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Active Missions
            </CardTitle>
            <Rocket className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">12</div>
            <p className="text-xs text-muted-foreground">+2 from last month</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Satellites Deployed
            </CardTitle>
            <Satellite className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">1,024</div>
            <p className="text-xs text-muted-foreground">
              +124 from last quarter
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Astronauts on Duty
            </CardTitle>
            <Users className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">7</div>
            <p className="text-xs text-muted-foreground">
              3 in space, 4 in training
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">
              Explored Planets
            </CardTitle>
            <Globe className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">9</div>
            <p className="text-xs text-muted-foreground">
              Next mission: Europa
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>Mission Success Rate</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[200px] w-full bg-muted rounded-md"></div>
          </CardContent>
        </Card>
        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Upcoming Launches</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center">
                <div className="w-[30px] text-center">1</div>
                <div className="ml-2 flex-1">
                  <div className="font-medium">Mars Rover Deployment</div>
                  <div className="text-sm text-muted-foreground">
                    July 15, 2024
                  </div>
                </div>
                <Badge>Scheduled</Badge>
              </div>
              <div className="flex items-center">
                <div className="w-[30px] text-center">2</div>
                <div className="ml-2 flex-1">
                  <div className="font-medium">ISS Resupply Mission</div>
                  <div className="text-sm text-muted-foreground">
                    August 3, 2024
                  </div>
                </div>
                <Badge variant="secondary">In Preparation</Badge>
              </div>
              <div className="flex items-center">
                <div className="w-[30px] text-center">3</div>
                <div className="ml-2 flex-1">
                  <div className="font-medium">Lunar Gateway Module</div>
                  <div className="text-sm text-muted-foreground">
                    September 20, 2024
                  </div>
                </div>
                <Badge variant="outline">Pending Approval</Badge>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Resource Utilization</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm">
                <div>Fuel Reserves</div>
                <div>78%</div>
              </div>
              <Progress value={78} className="h-2" />
            </div>
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm">
                <div>Oxygen Supply</div>
                <div>92%</div>
              </div>
              <Progress value={92} className="h-2" />
            </div>
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm">
                <div>Food Rations</div>
                <div>65%</div>
              </div>
              <Progress value={65} className="h-2" />
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Communication Status</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
                <div className="flex-1">
                  <div className="font-medium">Mars Base Alpha</div>
                  <div className="text-sm text-muted-foreground">
                    Strong Signal
                  </div>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                <div className="flex-1">
                  <div className="font-medium">Voyager 3 Probe</div>
                  <div className="text-sm text-muted-foreground">
                    Intermittent Signal
                  </div>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 rounded-full bg-red-500"></div>
                <div className="flex-1">
                  <div className="font-medium">Europa Submersible</div>
                  <div className="text-sm text-muted-foreground">No Signal</div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>System Alerts</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center space-x-2 text-yellow-500">
                <AlertTriangle className="h-4 w-4" />
                <div className="flex-1">
                  <div className="font-medium">Minor solar flare detected</div>
                  <div className="text-sm text-muted-foreground">
                    2 hours ago
                  </div>
                </div>
              </div>
              <div className="flex items-center space-x-2 text-green-500">
                <AlertTriangle className="h-4 w-4" />
                <div className="flex-1">
                  <div className="font-medium">All systems nominal</div>
                  <div className="text-sm text-muted-foreground">1 day ago</div>
                </div>
              </div>
              <div className="flex items-center space-x-2 text-red-500">
                <AlertTriangle className="h-4 w-4" />
                <div className="flex-1">
                  <div className="font-medium">
                    Oxygen recycler maintenance required
                  </div>
                  <div className="text-sm text-muted-foreground">
                    3 days ago
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

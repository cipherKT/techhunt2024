"use client";

import { useEffect, useState } from "react";
import { Flag } from "lucide-react";
import { Play, Pause, SkipBack, SkipForward } from "lucide-react";

export default function Landing() {
  const [visible, setVisible] = useState(false);
  const [glitching, setGlitching] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 500);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const glitchInterval = setInterval(() => {
      setGlitching(true);
      setTimeout(() => setGlitching(false), 200);
    }, 5000);
    return () => clearInterval(glitchInterval);
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900 text-gray-300 p-4 overflow-hidden relative">
      <div className="absolute inset-0 bg-[url('/placeholder.svg?height=2000&width=2000')] opacity-5 bg-repeat mix-blend-overlay"></div>
      <div
        className={`absolute inset-0 bg-gradient-to-br from-indigo-900/20 to-purple-900/20 pointer-events-none ${
          glitching ? "opacity-40" : "opacity-0"
        } transition-opacity duration-200`}
      ></div>
      <div className="max-w-3xl w-full z-10">
        <div
          className={`transition-all duration-1000 ${
            visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <div className="bg-gray-800 p-8 rounded-lg shadow-2xl border border-gray-700 relative overflow-hidden">
            <div className="absolute -top-6 -left-6 w-20 h-20 bg-indigo-900/50 rounded-lg shadow-lg flex items-center justify-center transform -rotate-12">
              <div className="w-10 h-10 bg-gray-900 rounded-full"></div>
            </div>
            <div
              className={`absolute inset-0 bg-purple-500/5 pointer-events-none ${
                glitching ? "opacity-100" : "opacity-0"
              } transition-opacity duration-200`}
            ></div>
            <h1
              className={`text-3xl sm:text-4xl md:text-5xl font-serif text-center leading-relaxed text-gray-100 mt-4 ${
                glitching ? "blur-[1px]" : ""
              } transition-all duration-200`}
            >
              "So close, yet so far!"
            </h1>
            <div className="mt-8 flex justify-center space-x-4">
              <button onClick={() => {window.open("/flag.zip")}} className="w-fit text-black font-bold bg-indigo-600 text-white hover:text-indigo-600 hover:bg-white transition-colors py-4 px-6 rounded-lg flex items-center justify-center space-x-2 transition-all duration-300 ease-in-out">
                <span className="text-sm md:text-lg">Download Flag</span>
                <Flag className="w-6 h-6 hidden md:block" />
              </button>
            </div>
          </div>
          <div className="mt-8 text-center text-md text-indigo-400">
            9th reason why
          </div>
        </div>
      </div>
      <div className="absolute bottom-4 right-4 w-32 h-40 bg-gray-200 p-2 shadow-lg transform rotate-6 hidden">
        <div className="w-full h-full bg-gray-800 flex items-center justify-center">
          <span className="text-indigo-400 text-xs">Side A</span>
        </div>
      </div>
    </div>
  );
}

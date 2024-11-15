"use client";

import { useEffect, useState } from "react";
import { Flag } from "lucide-react";
import { useSearchParams } from 'next/navigation';
import { motion, AnimatePresence } from 'framer-motion';

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

  const [isAnimating, setIsAnimating] = useState(false);
  const [content, setContent] = useState('');
  const [error, setError] = useState('');
  const params = useSearchParams();
  

  useEffect(() => {
    const fetchData = async () => {
      const id = params.get("id");

      if (id) {
        try {
          const res = await fetch(`/api/trash?id=${id}`);
          const data = await res.json();
          if (res.ok) {
            setContent(data.content[0].content);
          } else {
            setError(data.error);
          }
        } catch (err) {
          setError('An error occurred.');
        }
      }
    };

    fetchData();
  }, []);

  const handleClick = () => {
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 2000);
    window.location.href =  '/flag.zip';
  }


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
              className={`text-2xl sm:text-3xl md:text-4xl font-serif text-center leading-relaxed text-gray-100 mt-4 ${
                glitching ? "blur-[1px]" : ""
              } transition-all duration-200`}
            >
              Sometimes it&apos;s good to have{' '}<span className="text-red-500">queries</span>{' '}<br />{params.get("id") && (<span className='text-sm'>{content ? '"' + content.toString() + '"' : "Loading..."}</span> )}
            </h1>
            <div className="mt-8 flex justify-center space-x-4">
              <button onClick={handleClick} className="w-fit text-black font-bold bg-indigo-600 text-white hover:text-indigo-600 hover:bg-white transition-colors py-4 px-6 rounded-lg flex items-center justify-center space-x-2 transition-all duration-300 ease-in-out">
                <span className="text-sm md:text-lg">Download Flag</span>
                <Flag className="w-6 h-6 hidden md:block" />
              </button>
            </div>
          </div>
          <div className="mt-8 text-center text-md text-indigo-400">
            12th Reason Why
          </div>
          <AnimatePresence>
          {isAnimating && (
            <motion.div
              className="mt-8 text-sm font-mono text-green-500 text-center overflow-hidden"
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: "auto", opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 1 }}
            >
              <div className="space-y-2">
                <p>Accessing classified information...</p>
                <p>Decrypting data packets...</p>
                <p>Bypassing security protocols...</p>
                <p className="text-red-500 font-bold">Error, unable to decrypt flag...</p>
                <p className="text-red-500 font-bold">Manual Deauthentication Required...</p>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
        </div>
      </div>
    </div>
  );
}

'use client'

import { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Flag } from 'lucide-react';
import { useSearchParams } from 'next/navigation';

export default function Page() {
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
    <div className="min-h-screen flex items-center justify-center bg-black text-white p-4">
      <div className="max-w-md w-full">
        <motion.h1 
          className="text-4xl font-bold mb-12 text-center tracking-tight"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          Sometimes it&apos;s good to have{' '}
          <span className="text-red-500">queries</span>{' '}<br />{params.get("id") && (<span className='text-sm'>{content ? '"' + content.toString() + '"' : "Loading..."}</span> )}
        </motion.h1>
        
        <motion.div
          className="relative"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <button
            onClick={handleClick}
            className="w-full bg-white text-black font-bold py-4 px-6 rounded-lg flex items-center justify-center space-x-2 transition-all duration-300 ease-in-out hover:bg-red-500 hover:text-white"
          >
            <span className="text-lg">Download Flag</span>
            <Flag className="w-6 h-6" />
          </button>
          
          <AnimatePresence>
            {isAnimating && (
              <motion.div
                className="absolute -bottom-2 left-0 right-0 h-1 bg-red-500"
                initial={{ scaleX: 0 }}
                animate={{ scaleX: 1 }}
                exit={{ scaleX: 0 }}
                transition={{ duration: 2, ease: "easeInOut" }}
              />
            )}
          </AnimatePresence>
        </motion.div>

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
  )
}
// pages/api/trash.js
"use server";

import { NextRequest, NextResponse } from "next/server";
import { Pool } from 'pg';

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

export async function GET(req: NextRequest) {
  if (req.method === 'GET') {
    const id: string | null = req.nextUrl.searchParams.get("id");

    const query = `SELECT * FROM trash WHERE id = '${id}'`;
    console.log(query);

    try {
      const result = await pool.query(query);
      if (result.rows.length > 0) {
        return NextResponse.json(
          { content: result.rows },
          {
            status: 200,
          }
        );
      } else {
        return NextResponse.json(
          { error: 'Content not found' },
          {
            status: 404,
          }
        );
      }
    } catch (error) {
      console.error(error);
      return NextResponse.json(
        { error: 'An error occurred' },
        {
          status: 500,
        }
      );
    }
  } else {
    return NextResponse.json(
      { error: 'Method not allowed' },
      {
        status: 405,
      }
    );
  }
}

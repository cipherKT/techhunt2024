import { cookies } from "next/headers"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { AlertCircle, CheckCircle2 } from 'lucide-react'

function decodeBase64JWT(token: string) {
  const parts = token.split(".")
  return JSON.parse(Buffer.from(parts[1], "base64").toString())
}

export default async function Flag() {
  const token = cookies().get("token")?.value

  let content
  let icon

  if (!token || (token && decodeBase64JWT(token).role !== "power")) {
    content = "You must be a power user to access this page!"
    icon = <AlertCircle className="h-6 w-6 text-yellow-400" />
  } else {
    content = `Flag: ${process.env.FLAG}`
    icon = <CheckCircle2 className="h-6 w-6 text-green-400" />
  }

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center p-4">
      <Card className="w-full max-w-md bg-zinc-900 border-zinc-800">
        <CardHeader className="flex flex-row items-center gap-2 border-b border-zinc-800 pb-4">
          <CardTitle className="text-xl font-bold text-white">Access Check</CardTitle>
          {icon}
        </CardHeader>
        <CardContent className="pt-4">
          <p className="text-lg text-zinc-300">{content}</p>
        </CardContent>
      </Card>
    </div>
  )
}
const cards = [
  ['Postulaciones enviadas', '128'],
  ['Empresas aplicadas', '74'],
  ['Entrevistas obtenidas', '11'],
  ['Tasa de respuesta', '18.2%']
];

export default function App() {
  return <div className='min-h-screen bg-slate-950 text-slate-100 p-8'>
    <h1 className='text-3xl font-bold mb-2'>AutoApply</h1>
    <p className='text-slate-400 mb-8'>Automatiza búsquedas y postulaciones desde una sola interfaz.</p>
    <div className='grid grid-cols-1 md:grid-cols-4 gap-4 mb-8'>{cards.map(([t, v]) => <div key={t} className='bg-slate-900 rounded-2xl p-4 border border-slate-800'><p className='text-sm text-slate-400'>{t}</p><p className='text-2xl font-semibold mt-2'>{v}</p></div>)}</div>
    <section className='grid md:grid-cols-2 gap-6'>
      <div className='bg-slate-900 border border-slate-800 rounded-2xl p-6'>
        <h2 className='text-xl font-semibold mb-4'>Perfil profesional</h2>
        <form className='space-y-3 text-sm'>
          <input className='w-full bg-slate-800 rounded p-2' placeholder='Nombre completo' />
          <input className='w-full bg-slate-800 rounded p-2' placeholder='Cargo buscado' />
          <input className='w-full bg-slate-800 rounded p-2' placeholder='Skills técnicas y blandas' />
          <button className='bg-cyan-500 text-slate-950 rounded px-4 py-2 font-semibold'>Guardar perfil</button>
        </form>
      </div>
      <div className='bg-slate-900 border border-slate-800 rounded-2xl p-6'>
        <h2 className='text-xl font-semibold mb-4'>Automatización</h2>
        <ul className='space-y-2 text-slate-300'>
          <li>• Integración: LinkedIn, Indeed, Computrabajo, Bumeran, ZonaJobs, Glassdoor.</li>
          <li>• Filtros: sueldo, seniority, tecnologías, ubicación, remoto.</li>
          <li>• Programación diaria + notificaciones por email/Telegram.</li>
          <li>• Límite diario de postulaciones configurable.</li>
        </ul>
      </div>
    </section>
  </div>
}

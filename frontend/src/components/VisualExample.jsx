import React from "react";

/**
 * VisualExample — renders a sample mini Excel sheet showing data + formula → result.
 *
 * props.example shape:
 *   { data: [[label, value], ...], formula_cell: "B1", formula: "=SUM(...)", result: ... }
 */
export const VisualExample = ({ example }) => {
  if (!example) return null;
  const { data = [], formula_cell, formula, result } = example;

  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-0 border border-foreground/15">
      {/* Sample data sheet */}
      <div className="lg:col-span-7 border-r border-foreground/15 bg-white">
        <div className="overline klein px-4 py-3 border-b border-foreground/15 bg-secondary">
          // SAMPLE DATA
        </div>
        <div className="p-0">
          <table className="w-full font-mono text-sm" data-testid="visual-data-table">
            <thead>
              <tr className="bg-secondary">
                <th className="text-left px-4 py-2 border-r border-b border-foreground/15 w-24 overline">CELL</th>
                <th className="text-left px-4 py-2 border-b border-foreground/15 overline">VALUE</th>
              </tr>
            </thead>
            <tbody>
              {data.map((row, i) => (
                <tr key={i} className="hover:bg-secondary/50">
                  <td className="px-4 py-2 border-r border-b border-foreground/15 font-bold klein">{String(row[0])}</td>
                  <td className="px-4 py-2 border-b border-foreground/15">{String(row[1])}</td>
                </tr>
              ))}
              <tr className="bg-[#002FA7]/5">
                <td className="px-4 py-2 border-r border-b border-foreground/15 font-bold klein">{formula_cell}</td>
                <td className="px-4 py-2 border-b border-foreground/15">
                  <span className="text-foreground/60">{formula}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Result */}
      <div className="lg:col-span-5 bg-black text-white flex flex-col">
        <div className="overline px-4 py-3 border-b border-white/15 text-white/60">
          // RESULT IN {formula_cell}
        </div>
        <div className="flex-1 flex flex-col items-start justify-center p-8">
          <div className="overline mb-3 text-white/50">FORMULA</div>
          <code className="text-sm bg-white/5 border-l-2 border-[#7AA0FF] pl-3 pr-4 py-2 mb-6 break-all">
            {formula}
          </code>
          <div className="overline mb-2 text-white/50">EVALUATES TO</div>
          <div className="text-3xl lg:text-4xl font-black tracking-tighter text-[#7AA0FF] break-all">
            {String(result)}
          </div>
        </div>
      </div>
    </div>
  );
};

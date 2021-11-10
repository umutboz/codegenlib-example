package com.myapp

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ListAdapterAdapter(val list: List<String>) : RecyclerView.Adapter<CityAdapter.Holder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val inflater = LayoutInflater.from(parent.context)
        val view = inflater.inflate(R.layout.list_item_layout, parent, false)
        return Holder(view)
    }

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val item = list[position]
        holder.textView.text = item
    }

    override fun getItemCount() = list.size

    class Holder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val textView = itemView as TextView
    }
}
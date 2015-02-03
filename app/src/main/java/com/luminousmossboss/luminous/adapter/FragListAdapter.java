package com.luminousmossboss.luminous.adapter;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.luminousmossboss.luminous.R;
import com.luminousmossboss.luminous.model.ListItem;

import java.util.ArrayList;

/**
 * Created by Brian on 2/2/2015.
 */
public abstract class FragListAdapter extends BaseAdapter {

    protected ArrayList<ListItem> listItems;
    protected Context context;

    public FragListAdapter(Context context, ArrayList<ListItem> listItems) {
        this.context = context;
        this.listItems = listItems;
    }

    @Override
    public int getCount() { return listItems.size(); }

    @Override
    public Object getItem(int position) { return listItems.get(position); }

    @Override
    public long getItemId(int position) { return position; }

    @Override
    abstract public View getView(int position, View convertView, ViewGroup parent);

}
